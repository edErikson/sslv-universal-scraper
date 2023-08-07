# Project Description

This project is a web scraper designed to scrape data from the SS.lv website, a popular classifieds site. This scraper is able to collect information on various types of listings, including computers, cars, furniture, or real estate, based on the URL provided. The scraped data is stored as CSV files for convenient processing and analysis.

The scraper uses Python's `requests` library to fetch web pages and `BeautifulSoup` to parse the HTML and extract the desired data. It includes features to navigate to and scrape data from multiple pages of listings. Additionally, it includes a function to save the scraped data to a CSV file, with the filename generated based on the category of the listings being scraped.

# Readme File for GitHub

```markdown
# SS.lv Web Scraper

## Description

This project is a web scraper built in Python that scrapes data from the SS.lv website, a popular classifieds site. The scraper can fetch details from multiple categories of listings like computers, cars, furniture, real estate, etc. based on the URL provided. The scraped data is then saved in CSV format for further processing and analysis.

## Dependencies

- Python 3.8+
- BeautifulSoup4
- requests

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/sslv-webscraper.git
   ```
2. Navigate into the project directory:
   ```bash
   cd sslv-webscraper
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script with a URL for the category you want to scrape:
   ```bash
   python main.py --url https://www.ss.lv/lv/electronics/computers/pc/
   ```
   This will scrape computer listings and save them to a file named `electronics_computers_pc.csv`.

## Note

This scraper is for educational purposes only. Before using it, make sure you understand and comply with the website's terms of service, as well as any applicable laws and regulations.
This web scraper is designed to extract data from listings pages on SS.lv. Navigate to the desired category on SS.lv until you reach a page with a list of items (like the example below), then copy and provide the URL to the scraper.

![Example of listings page on SS.lv](https://github.com/edErikson/sslv-universal-scraper/assets/38958077/e811cb94-d703-4dd4-bd71-994be4ade670)


## License

MIT
```

 `https://github.com/edErikson/sslv-webscraper.git`
