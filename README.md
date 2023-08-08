# SS.lv Web Scraper and Data Analysis

## Description

This project is a comprehensive toolset beginning with a web scraper built in Python that scrapes data from the SS.lv website, a popular classifieds site in Latvia. Post extraction, the data undergoes analysis and visualization to glean insights, particularly related to real estate listings.

Web Scraper
The scraper can fetch details from multiple categories of listings like computers, cars, furniture, real estate, etc. based on the URL provided. The scraped data is then saved in CSV format.

Data Analysis
The extracted real estate data is further analyzed using a Jupyter Notebook to understand trends and insights in the listings. Visualizations including maps are generated to better represent the data distribution across different districts.
## Dependencies

- Python 3.8+
- BeautifulSoup4
- requests

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/edErikson/sslv-universal-scraper
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

## Data Analysis
Navigate to the notebooks directory.

Open the Jupyter Notebook analysis.ipynb.

Execute the notebook cells for analysis and visualizations.

GeoJSON data, utilized for mapping, is in the data directory as riga_districts_final.geojson.

Generated visualization outputs are located in the output directory.

## Note

This scraper is for educational purposes only. Before using it, make sure you understand and comply with the website's terms of service, as well as any applicable laws and regulations.
This web scraper is designed to extract data from listings pages on SS.lv. Navigate to the desired category on SS.lv until you reach a page with a list of items (like the example below), then copy and provide the URL to the scraper.

![Example of listings page on SS.lv](https://github.com/edErikson/sslv-universal-scraper/assets/38958077/e811cb94-d703-4dd4-bd71-994be4ade670)


## License

MIT
```

https://github.com/edErikson/sslv-universal-scraper
