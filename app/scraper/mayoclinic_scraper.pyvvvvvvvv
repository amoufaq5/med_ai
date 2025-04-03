# app/scraper/mayoclinic_scraper.py
import requests
from bs4 import BeautifulSoup
import json
from app.config import MAYO_DRUGS_URL, SCRAPED_DATA_PATH

def scrape_mayoclinic_drugs():
    try:
        response = requests.get(MAYO_DRUGS_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # Extract relevant content (this is an example – adjust selectors accordingly)
        drugs = []
        for item in soup.select(".drug-listing"):
            title = item.get_text(strip=True)
            link = item.find("a")["href"] if item.find("a") else ""
            drugs.append({"title": title, "link": link})
        with open(f"{SCRAPED_DATA_PATH}/mayoclinic_drugs.json", "w") as f:
            json.dump(drugs, f, indent=2)
        print("Mayo Clinic drugs data scraped successfully.")
    except Exception as e:
        print(f"Error scraping Mayo Clinic drugs: {e}")

if __name__ == "__main__":
    scrape_mayoclinic_drugs()
