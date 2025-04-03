import requests
import json
from bs4 import BeautifulSoup
import os
from app.config import SCRAPED_DATA_PATH, DRUGS_OTC_URL

def scrape_drugs_com_otc():
    try:
        response = requests.get(DRUGS_OTC_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        drugs = []
        # Look for all links that include '/otc/' in their URL
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            if "/otc/" in href:
                drug_name = a_tag.get_text(strip=True)
                if drug_name:
                    drugs.append({"name": drug_name, "link": f"https://www.drugs.com{href}"})
        output_file = os.path.join(SCRAPED_DATA_PATH, "drugs_com_otc.json")
        with open(output_file, "w") as f:
            json.dump(drugs, f, indent=2)
        print(f"Successfully scraped Drugs.com OTC drugs. Data saved to {output_file}.")
    except Exception as e:
        print(f"Error scraping Drugs.com: {e}")

if __name__ == "__main__":
    scrape_drugs_com_otc()
