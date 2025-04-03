import requests
import json
from bs4 import BeautifulSoup
import os
from app.config import SCRAPED_DATA_PATH, MEDLINEPLUS_URL

def scrape_medlineplus_druginformation():
    try:
        response = requests.get(MEDLINEPLUS_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        drugs = []
        # Example: look for links with 'druginformation' in the URL
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            if "druginformation" in href.lower():
                drug_name = a_tag.get_text(strip=True)
                if drug_name:
                    drugs.append({"name": drug_name, "link": href})
        output_file = os.path.join(SCRAPED_DATA_PATH, "medlineplus_druginformation.json")
        with open(output_file, "w") as f:
            json.dump(drugs, f, indent=2)
        print(f"Successfully scraped MedlinePlus drug information. Data saved to {output_file}.")
    except Exception as e:
        print(f"Error scraping MedlinePlus: {e}")

if __name__ == "__main__":
    scrape_medlineplus_druginformation()
