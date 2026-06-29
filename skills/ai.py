import os
import time

from dotenv import load_dotenv
from google import genai

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

# ==========================================
# Conversation Memory
# ==========================================

chat_history = []

# ==========================================
# Build Conversation
# ==========================================

def build_conversation(prompt):

    system_prompt = """
You are MAX AI.

You are an intelligent desktop voice assistant.

Rules:
- Never say you are Gemini.
- Keep answers under 120 words.
- Speak naturally.
- Help with coding.
- Help with studies.
- Help with daily life.
- Remember previous conversation.
"""

    conversation = system_prompt + "\n\n"

    for item in chat_history:
        conversation += f"{item['role']}: {item['text']}\n"

    conversation += f"User: {prompt}"

    return conversation


# ==========================================
# Ask Gemini
# ==========================================

def ask_ai(prompt):

    global chat_history

    conversation = build_conversation(prompt)

    models = [
        "gemini-2.5-flash-lite",
        "gemini-2.0-flash",
        "gemini-2.5-flash"
    ]

    for model_name in models:

        for attempt in range(3):

            try:

                print("\n🤖 MAX")
                print("🧠 Thinking...\n")

                for dots in ["●", "●●", "●●●"]:
                    print(f"Connecting {dots}")
                    time.sleep(0.3)

                print(f"\n⚡ Using {model_name}\n")

                response = client.models.generate_content(
                    model=model_name,
                    contents=conversation
                )

                answer = response.text.strip()

                # Keep spoken response short
                sentences = answer.split(". ")

                if len(sentences) > 4:
                    answer = ". ".join(sentences[:4]) + "."

                # Save conversation
                chat_history.append({
                    "role": "User",
                    "text": prompt
                })

                chat_history.append({
                    "role": "MAX",
                    "text": answer
                })

                # Keep only last 20 messages
                chat_history = chat_history[-20:]

                print("✅ AI Response Ready\n")

                return answer

            except Exception as e:

                print(f"❌ {model_name} | Attempt {attempt + 1}: {e}")

                time.sleep(0.8)

    return (
        "Sorry, Google's AI service is busy right now. "
        "Please try again in a few moments."
    )