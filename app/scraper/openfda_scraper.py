# app/scraper/openfda_scraper.py
import requests
import json
from app.config import OPEN_FDA_URL, SCRAPED_DATA_PATH

def scrape_openfda():
    try:
        params = {"limit": 100}  # Adjust parameters as needed
        response = requests.get(OPEN_FDA_URL, params=params)
        response.raise_for_status()
        data = response.json()
        # Save to file
        with open(f"{SCRAPED_DATA_PATH}/openfda_data.json", "w") as f:
            json.dump(data, f, indent=2)
        print("openFDA data scraped successfully.")
    except Exception as e:
        print(f"Error scraping openFDA: {e}")

if __name__ == "__main__":
    scrape_openfda()
