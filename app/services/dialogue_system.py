# app/services/dialogue_system.py
def get_response(user_input, context={}):
    """
    A simple rule-based dialogue system.
    The context dictionary can include patient details and conversation history.
    """
    # Analyze input to extract key symptoms and context – here, we use simple keyword matching.
    response = ""
    if "pain" in user_input.lower():
        response += "It sounds like you are experiencing pain. "
    if "fever" in user_input.lower():
        response += "A fever may indicate an infection. "
    
    # Incorporate ASMETHOD steps
    response += "Please provide your age, if it is you or someone else, current medications, and how long the symptoms have persisted. "
    
    # Incorporate ENCORE (for example, if no medication is mentioned)
    if "medication" not in user_input.lower():
        response += "Could you tell me if you have taken any medications? "
    
    # Incorporate SIT DOWN SIR elements by asking follow-up questions
    response += "Also, where is the pain located and how severe is it on a scale of 1 to 10?"
    
    return response

if __name__ == "__main__":
    sample_input = "I have been having a fever and some pain."
    print(get_response(sample_input))
