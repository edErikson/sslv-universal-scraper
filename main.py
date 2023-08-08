import requests
from bs4 import BeautifulSoup
import csv
import time


def fetch_details(url):
    """
    Fetch detailed information about a listing from its individual page.

    Parameters:
    url (str): The URL of the listing's page.

    Returns:
    dict: A dictionary containing key-value pairs of the listing's details.
    """
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = {'URL': url}
    for row in soup.find_all('tr'):
        key_td = row.find('td', {'class': 'ads_opt_name'})
        value_td = row.find('td', {'class': 'ads_opt'})

        if key_td and value_td:  # Ensure both td elements are found
            key = key_td.text.strip()
            value = value_td.text.strip()
            data[key] = value

    # Extracting the price
    price_tag = soup.find('td', {'class': 'ads_price'})
    if price_tag:
        data['Cena'] = price_tag.text.strip()

    return data


def fetch_listings(url):
    """
    Fetch all listings from a page and their detailed information.

    Parameters:
    url (str): The URL of the page containing the listings.

    Returns:
    list: A list of dictionaries, each containing detailed information about a listing.
    """
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    listings = []

    # Selecting all rows that represent property details
    for tr in soup.select('tr[id^="tr_"]'):

        # Extracting the link for each property
        detailed_link = tr.select_one('a.am')
        if detailed_link:
            link = "https://www.ss.lv" + detailed_link['href']
            listing_details = fetch_details(link)
            listings.append(listing_details)

    return listings


def fetch_all_listings(base_url):
    """
    Fetch all listings from a set of pages starting from a base URL.

    This function fetches listings from the provided URL and continues
    to fetch from subsequent pages until there are no more pages of listings.
    It uses a gentle sleep time to prevent overloading the server with requests.

    Parameters:
    base_url (str): The URL of the first page of listings.

    Returns:
    list: A list of dictionaries, each containing detailed information about a listing.
    """
    # Initial URL
    url = base_url
    prev_url = None  # To keep track of the previous page URL

    all_listings = []  # renaming from 'all_flats'

    page_number = 1

    while True:
        # Fetch listings on current page
        listings = fetch_listings(url)  # renaming from 'flats'
        all_listings.extend(listings)  # renaming from 'all_flats'

        print(f"Fetched {len(listings)} listings from this page.")

        # Fetch the page content
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check for next page link
        next_page_tag = soup.find('a', {'name': 'nav_id', 'rel': 'next'})

        # Break if there is no next page or if the next URL is the same as the current URL
        if not next_page_tag or url == "https://www.ss.lv" + next_page_tag['href'] or "https://www.ss.lv" + \
                next_page_tag['href'] == base_url or "https://www.ss.lv" + next_page_tag['href'] == prev_url:
            break

        # Otherwise, update the URLs and proceed
        prev_url = url
        url = "https://www.ss.lv" + next_page_tag['href']

        print(f"Moving to next page: {url}")

        # Pause to be gentle on server
        time.sleep(0.5)

        page_number += 1

    return all_listings


def save_to_csv(all_property_data, filename):
    # Create a set to store all the keys
    headers = set()
    # Iterate over all dictionaries and add their keys to the set
    for data in all_property_data:
        headers.update(data.keys())
    # Convert the set to a list, so it can be used as fieldnames in the csv writer
    headers = list(headers)
    # Open the file in write mode ('w') and create a csv writer object
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        # Write the headers to the CSV
        writer.writeheader()
        # Write each dictionary from the list to the CSV
        for data in all_property_data:
            writer.writerow(data)


if __name__ == '__main__':
    session = requests.Session()
    # main_url = 'https://www.ss.lv/lv/electronics/computers/pc/'
    # main_url = 'https://www.ss.lv/lv/home-stuff/furniture-interior/sofas/'
    main_url = 'https://www.ss.lv/lv/real-estate/flats/riga/all/sell/'
    all_listings_data = fetch_all_listings(main_url)
    # Extract parts of the URL and create filename
    parts = main_url.split('/')[4:-1]  # [4:-1] to exclude 'https:', '', 'www.ss.lv', 'lv', and the last empty part
    filename = "_".join(parts) + ".csv"
    print(f"Total number of listings scraped: {len(all_listings_data)}")
    save_to_csv(all_listings_data, 'data/' + filename)
