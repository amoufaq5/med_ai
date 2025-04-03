# app/ui/chatbot_ui.py
from flask import Flask, render_template, request, jsonify
from app.services import dialogue_system, diagnosis

app = Flask(__name__)

# Route for the chatbot UI
@app.route("/")
def index():
    return render_template("index.html")

# API endpoint for chatbot interaction
@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    # Use dialogue system to generate a response
    response_text = dialogue_system.get_response(user_input)
    return jsonify({"response": response_text})

# API endpoint for submitting patient data for diagnosis
@app.route("/api/diagnose", methods=["POST"])
def diagnose():
    patient_data = request.json
    result = diagnosis.diagnose(patient_data)
    return jsonify({"diagnosis": result})

if __name__ == "__main__":
    # In production, consider using gunicorn or another WSGI server
    app.run(host="0.0.0.0", port=5000, debug=False)
