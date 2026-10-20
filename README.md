# 🛡️ Cyber Aware Bot

An interactive, RAG (Retrieval-Augmented Generation) cybersecurity teaching assistant. 

## 🎯 The Problem
Generic AI chatbots are prone to "hallucinations" (making up facts). In cybersecurity, inaccurate advice (e.g., how to handle a phishing email) can lead to severe security breaches. 

## 💡 The Solution
Cyber Aware Bot solves this by using a **RAG architecture**. Instead of relying solely on the LLM's pre-trained knowledge, the bot searches a locally curated database of authoritative cybersecurity documents (`docs/`) before generating an answer. This ensures all advice is grounded, accurate, and verifiable.

## 🏗️ Architecture Diagram
```text
[User Question] 
      │
      ▼
[Local Vector Search (docs/)] ──> Retrieves relevant cybersecurity context
      │
      ▼
[Google Gemini API] ──> Generates answer based *only* on context
      │
      ▼
[Answer + Source Citation]
