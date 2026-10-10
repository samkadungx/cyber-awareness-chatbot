from dotenv import load_dotenv
from cofone import RAG

# Load the API key from your .env file
load_dotenv()

# 1. Initialize the RAG system using Gemini
# The unsupported 'search' parameter has been removed to fix the TypeError
rag = RAG(model_provider="gemini", model="gemini-3.8-flash")

# 2. Tell it where the knowledge is
rag.add_source("docs/")

print("🤖 Cyber Aware Bot is ready! (Type 'quit' to exit)")
print("-" * 40)

# 3. Simple chat loop
while True:
    user_question = input("\nYou: ")
    
    if user_question.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break
        
    if not user_question.strip():
        continue

    # 4. Get the answer (RAG does the retrieval + generation)
    try:
        print("Bot is thinking and searching docs... please wait.")
        answer = rag.run(user_question)
        print(f"\nBot: {answer}")
    except Exception as e:
        print(f"\nBot: Sorry, I ran into an error: {e}")