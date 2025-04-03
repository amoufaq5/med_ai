# app/scraper/imaging_scraper.py
import requests
import os
from app.config import SCRAPED_DATA_PATH

def scrape_imaging_data():
    try:
        # Example: downloading sample images from a public source
        image_urls = [
            "https://www.example.com/ct_sample1.jpg",
            "https://www.example.com/mri_sample1.jpg"
        ]
        image_folder = os.path.join(SCRAPED_DATA_PATH, "imaging")
        os.makedirs(image_folder, exist_ok=True)
        for url in image_urls:
            image_data = requests.get(url).content
            filename = os.path.join(image_folder, url.split("/")[-1])
            with open(filename, "wb") as f:
                f.write(image_data)
            print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Error scraping imaging data: {e}")

if __name__ == "__main__":
    scrape_imaging_data()
