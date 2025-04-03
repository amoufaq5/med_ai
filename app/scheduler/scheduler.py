# app/scheduler/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from app.scraper import openfda_scraper, clinical_trials_scraper, mayoclinic_scraper, imaging_scraper
import time

def start_scheduler():
    scheduler = BackgroundScheduler()
    # Schedule openFDA scraper to run every 6 hours
    scheduler.add_job(openfda_scraper.scrape_openfda, 'interval', hours=6)
    # Schedule clinical trials scraper every 12 hours
    scheduler.add_job(clinical_trials_scraper.scrape_clinical_trials, 'interval', hours=12)
    # Schedule Mayo Clinic scraper daily
    scheduler.add_job(mayoclinic_scraper.scrape_mayoclinic_drugs, 'interval', hours=24)
    # Schedule imaging data scraper daily
    scheduler.add_job(imaging_scraper.scrape_imaging_data, 'interval', hours=24)
    scheduler.start()
    print("Scheduler started. Scraping jobs are scheduled.")
    
    try:
        # Keep the main thread alive.
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Scheduler shutdown.")

if __name__ == "__main__":
    start_scheduler()
