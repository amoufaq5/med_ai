# app/services/diagnosis.py
def diagnose(patient_data):
    """
    patient_data: dict containing keys such as 'age', 'symptoms', 'duration', 'severity', etc.
    Uses ASMETHOD, ENCORE, and SIT DOWN SIR frameworks to determine next steps.
    """
    # Basic rule-based decision logic:
    if "chest pain" in patient_data.get("symptoms", "").lower() and patient_data.get("severity", 0) > 7:
        return "Your symptoms are concerning. I recommend you seek immediate medical attention."
    elif "fever" in patient_data.get("symptoms", "").lower() and patient_data.get("duration", 0) > 3:
        return "It seems like you have a persistent fever. Please consider consulting a doctor for further evaluation."
    else:
        return "Based on the information provided, it may be a common illness. Monitor your symptoms and if they worsen, see a healthcare provider."

if __name__ == "__main__":
    sample_patient = {
        "age": 45,
        "symptoms": "chest pain, shortness of breath",
        "duration": 1,
        "severity": 8,
    }
    print(diagnose(sample_patient))
