# LLM-Powered Prompt Router for Intent Classification

## Overview

This project implements an AI-based prompt routing system that detects a user’s intent and routes the request to a specialized AI persona.

Instead of relying on a single monolithic prompt, the system follows a two-step architecture:

1. Classify the user’s intent
2. Delegate the request to an expert assistant

The system supports multiple expert personas such as Code Expert, Data Analyst, Writing Coach, and Career Advisor. This approach improves response quality, ensures focused outputs, and enables scalable multi-purpose AI systems.

---

## System Architecture

```
User Message
      ↓
Intent Classification (LLM Call 1)
      ↓
Intent + Confidence (JSON)
      ↓
Prompt Router
      ↓
Select Expert Persona
      ↓
Response Generation (LLM Call 2)
      ↓
Final Response
      ↓
Logging (route_log.jsonl)
```

---

## System Workflow

1. The user sends a message.
2. The `classify_intent` function sends it to a lightweight LLM.
3. The LLM returns a structured JSON object containing intent and confidence.
4. The router selects the appropriate expert system prompt.
5. A second LLM call generates the final response using the selected persona.
6. If the intent is unclear, the system asks a clarification question instead of making assumptions.
7. Every request is logged in `route_log.jsonl` for observability.

---

## Supported Intents

**Code**
Programming questions, debugging, algorithms, or software development tasks.

**Data**
Questions involving statistics, SQL queries, datasets, or data interpretation.

**Writing**
Requests for feedback on clarity, tone, grammar, or structure.

**Career**
Questions related to job interviews, resumes, career planning, or professional growth.

**Unclear**
Messages that are ambiguous or do not clearly match any supported category.

---

## Project Structure

```
.
├── main.py
├── classifier.py
├── router.py
├── prompts.py
├── logger.py
├── test_messages.py
├── route_log.jsonl
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Example Outputs

### Classifier Output

```json
{
  "intent": "code",
  "confidence": 0.92
}
```

### Log Entry

```json
{
  "intent": "writing",
  "confidence": 0.88,
  "user_message": "my writing is too verbose",
  "final_response": "..."
}
```

Each line in `route_log.jsonl` represents a single processed request.

---

## Technologies Used

* Python
* OpenAI API
* Prompt Engineering
* JSON Parsing
* Intent-Based Routing Architecture

---

## Conclusion

This project demonstrates a scalable AI design pattern where user intent is first classified and then routed to specialized prompts.

By separating intent detection from response generation, the system produces more accurate, context-aware, and high-quality outputs compared to traditional single-prompt approaches.

