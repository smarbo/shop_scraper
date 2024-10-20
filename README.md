# ShopScraper
-- A simple web scraper script which compares the price of a product at 2 different stores.

## Installation
```bash
git clone https://github.com/smarbo/shop_scraper
cd shop_scraper
pip install selenium beautifulsoup4
```
## Usage
Make sure you have a chrome driver installed which is required to run Selenium and emulate a chrome browser to fetch the data.
This can be installed [here](https://developer.chrome.com/docs/chromedriver/get-started)
Then, all you have to do is:
```
python3 main.py
```
The script will ask you for a product search query, and then fetch the data from each store (This will take a while) and give you a comparison.

### Enjoy!
