# app/config.py
import os

# API endpoints and web URLs for scraping
OPEN_FDA_URL = "https://api.fda.gov/drug/drugsfda.json"
CLINICAL_TRIALS_API = "https://clinicaltrials.gov/api/v2"
MAYO_DRUGS_URL = "https://www.mayoclinic.org/drugs-supplements"
MAYO_DISEASES_URL = "https://www.mayoclinic.org/diseases-conditions"
MAYO_SYMPTOMS_URL = "https://www.mayoclinic.org/symptoms"
DRUGS_OTC_URL = "https://www.drugs.com/otc/"
MEDLINEPLUS_URL = "https://medlineplus.gov/druginformation.html"
DAILYMED_DRUGNAMES_URL = "https://www.dailymed.nlm.nih.gov/dailymed/webservices-help/v2/drugnames_api.cfm#XML"
DAILYMED_DRUGCLASSES_URL = "https://www.dailymed.nlm.nih.gov/dailymed/webservices-help/v2/drugclasses_api.cfm#XML"
WEBMD_URL = "https://www.webmd.com/drugs/2/index"

# Imaging additional sources (placeholders)
CT_SCAN_SOURCE = "https://www.examplectsource.com"
MRI_SOURCE = "https://www.examplemrisource.com"

# Data paths
SCRAPED_DATA_PATH = os.path.join(os.getcwd(), "data", "scraped_data")
TRAINED_MODELS_PATH = os.path.join(os.getcwd(), "data", "trained_models")

# HIPAA and security settings (to be expanded)
SECURITY_SETTINGS = {
    "enable_encryption": True,
    "data_retention_days": 365,
}

# Set the base directory to E:\med_ai
BASE_PATH = r"E:\med_ai"


