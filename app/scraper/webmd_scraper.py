import requests
import json
from bs4 import BeautifulSoup
import os
from app.config import SCRAPED_DATA_PATH, WEBMD_URL

def scrape_webmd():
    try:
        response = requests.get(WEBMD_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        drugs = []
        # Find links that include 'drug' in the URL; adjust the filter as necessary
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            if "drug" in href.lower():
                drug_name = a_tag.get_text(strip=True)
                if drug_name:
                    if not href.startswith("http"):
                        href = "https://www.webmd.com" + href
                    drugs.append({"name": drug_name, "link": href})
        output_file = os.path.join(SCRAPED_DATA_PATH, "webmd_drugs.json")
        with open(output_file, "w") as f:
            json.dump(drugs, f, indent=2)
        print(f"Successfully scraped WebMD drugs. Data saved to {output_file}.")
    except Exception as e:
        print(f"Error scraping WebMD: {e}")

if __name__ == "__main__":
    scrape_webmd()
