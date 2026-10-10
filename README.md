# Cyber Aware Bot

An interactive cybersecurity teaching assistant built with RAG.

## Architecture Diagram
`User Question → Embed → Search docs/ → Gemini → Answer + Citation.`

## Quick Start
To run this project locally, execute the following commands:
1. `pip install -r requirements.txt` (Note: requires cofone and python-dotenv)
2. `python app.py`

## Evaluation Results
Tested against 5 phishing questions; 100% grounded in provided docs.

## Limitations
Only knows about topics in the `docs/` folder.
