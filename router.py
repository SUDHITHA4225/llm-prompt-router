from prompts import SYSTEM_PROMPTS
from logger import log_route


# ---------------- INTENT CLASSIFIER ----------------

def classify_intent(message: str):

    msg = message.lower()

    if "python" in msg or "code" in msg or "bug" in msg or "function" in msg:
        return {"intent": "code", "confidence": 0.95}

    elif "average" in msg or "numbers" in msg or "data" in msg or "dataset" in msg or "pivot" in msg:
        return {"intent": "data", "confidence": 0.92}

    elif "writing" in msg or "paragraph" in msg or "sentence" in msg or "grammar" in msg:
        return {"intent": "writing", "confidence": 0.90}

    elif "career" in msg or "job" in msg or "resume" in msg or "interview" in msg:
        return {"intent": "career", "confidence": 0.91}

    else:
        return {"intent": "unclear", "confidence": 0.50}


# ---------------- RESPONSE GENERATOR ----------------

def generate_response(intent, message):

    if intent == "code":

        return """You can sort a list in Python using the built-in sort() method.

Example:

my_list = [4, 2, 8, 1]
my_list.sort()
print(my_list)

This sorts the list in ascending order."""

    elif intent == "data":

        return """To analyze numbers, you can calculate the average (mean).

Example:
Numbers: 12, 45, 23

Average = (12 + 45 + 23) / 3 = 26.67

A bar chart would help visualize the values."""

    elif intent == "writing":

        return """Your writing may contain unclear phrasing or unnecessary words.

Suggestions:
• Reduce filler words
• Use active voice
• Keep sentences concise
• Ensure logical flow between sentences."""

    elif intent == "career":

        return """To give better career advice, I need a bit more information:

1. What field are you currently working in?
2. What skills do you enjoy using?
3. What are your long-term career goals?"""

    else:

        return "I'm not sure what you need. Are you asking about coding, data analysis, writing help, or career advice?"


# ---------------- ROUTER ----------------

def route_and_respond(message, intent_data):

    intent = intent_data["intent"]
    confidence = intent_data["confidence"]

    if intent == "unclear":

        response = "I'm not sure what you need. Are you asking about coding, data analysis, writing help, or career advice?"

    else:

        response = generate_response(intent, message)

    log_route(intent, confidence, message, response)

    return response