**LLM-Powered Prompt Router for Intent Classification**

---

**Overview**

This project implements an AI prompt routing system that detects a user’s intent and routes the request to a specialized AI persona. Instead of using one large prompt for all tasks, the system first classifies the user message and then delegates it to an expert assistant such as a **Code Expert**, **Data Analyst**, **Writing Coach**, or **Career Advisor**.
This architecture improves response quality, keeps prompts focused, and makes the system scalable for building multi-purpose AI applications.

---

**System Architecture**

User Message
↓
Intent Classification (LLM Call 1)
↓
Intent + Confidence (JSON Output)
↓
Prompt Router
↓
Select Expert Persona Prompt
↓
Response Generation (LLM Call 2)
↓
Final Response to User
↓
Log Routing Decision

---

**System Workflow**

1. The user sends a message to the system.
2. The **classify_intent** function sends the message to a lightweight LLM classifier.
3. The classifier returns a JSON object containing **intent** and **confidence**.
4. The router selects the appropriate expert system prompt based on the detected intent.
5. A second LLM call generates the final response using that expert persona.
6. If the intent is **unclear**, the system asks the user for clarification instead of guessing.
7. The system logs the routing decision and response in **route_log.jsonl**.

---

**Supported Intents**

**Code**
Programming questions, debugging, algorithms, or software development tasks.

**Data**
Questions involving numbers, statistics, SQL queries, datasets, or data interpretation.

**Writing**
Requests for feedback on writing clarity, tone, grammar, or structure.

**Career**
Questions related to job interviews, resumes, career planning, or professional growth.

**Unclear**
Messages that are ambiguous or do not clearly match any supported category.

---

**Project Structure**

main.py
Handles user input, runs classification, routes the request, and prints the response.

classifier.py
Implements the intent classification logic using an LLM and returns structured JSON.

router.py
Selects the correct expert prompt and generates the final response.

prompts.py
Stores all expert system prompts in a configurable dictionary.

logger.py
Logs routing decisions and responses into **route_log.jsonl**.

test_messages.py
Contains sample messages used for testing routing behavior.

requirements.txt
Lists project dependencies.

---

**Example Classifier Output**

{
"intent": "code",
"confidence": 0.92
}

---

**Example Log Entry**

{"intent":"writing","confidence":0.88,"user_message":"my writing is too verbose","final_response":"..."}

Each line in **route_log.jsonl** represents one request processed by the system.

---

**Technologies Used**

Python
OpenAI API
Prompt Engineering
JSON Parsing
Intent-Based Routing Architecture

---

**Conclusion**

This project demonstrates a practical AI architecture where user requests are first classified and then routed to specialized prompts. By separating **intent detection** and **response generation**, the system produces more accurate and context-aware responses while maintaining a modular and scalable design.
