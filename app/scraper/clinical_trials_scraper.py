# app/scraper/clinical_trials_scraper.py
import requests
import json
from app.config import CLINICAL_TRIALS_API, SCRAPED_DATA_PATH

def scrape_clinical_trials():
    try:
        # Example query: adjust parameters as per API docs
        params = {"cond": "cancer", "recr": "Open", "limit": 50}
        response = requests.get(f"{CLINICAL_TRIALS_API}/studies", params=params)
        response.raise_for_status()
        data = response.json()
        with open(f"{SCRAPED_DATA_PATH}/clinical_trials.json", "w") as f:
            json.dump(data, f, indent=2)
        print("Clinical trials data scraped successfully.")
    except Exception as e:
        print(f"Error scraping clinical trials: {e}")

if __name__ == "__main__":
    scrape_clinical_trials()
