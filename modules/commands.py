from intents.intent import detect_intent

from modules.speech import speak, listen

from skills.search import search
from skills.web import open_site
from skills.system import tell_time, tell_date
import skills.weather as weather
from skills.ai import ask_ai
from skills.reminder import set_reminder
from skills.email_service import send_email
from skills.custom_commands import execute_custom_command

import re


def execute(command):

    intent = detect_intent(command)

    # ==========================================
    # Greeting
    # ==========================================

    if intent == "GREETING":

        speak("Hello Nikijon. How can I help you today?")

    # ==========================================
    # Time
    # ==========================================

    elif intent == "TIME":

        tell_time()

    # ==========================================
    # Date
    # ==========================================

    elif intent == "DATE":

        tell_date()

    # ==========================================
    # Open Websites
    # ==========================================

    elif intent == "OPEN":

        open_site(command)

    # ==========================================
    # Google Search
    # ==========================================

    elif intent == "SEARCH":

        search(command)

    # ==========================================
    # Weather
    # ==========================================

    elif intent == "WEATHER":

        city = command.lower()

        city = city.replace("weather", "")
        city = city.replace("in", "")
        city = city.strip()

        if city == "":
            city = "Bhubaneswar"

        weather.get_weather(city)

    # ==========================================
    # Reminder
    # ==========================================

    elif intent == "REMINDER":

        match = re.search(r"(\d+)", command)

        if not match:

            speak("Please tell me after how many seconds.")

        else:

            seconds = int(match.group())

            message = command

            message = message.replace("remind me to", "")

            message = re.sub(r"in \d+ seconds?", "", message)

            message = message.strip()

            if message == "":
                message = "This is your reminder."

            set_reminder(seconds, message)

    # ==========================================
    # Email
    # ==========================================

    elif intent == "EMAIL":

        speak("Please type the recipient email in the terminal.")

        print("\n" + "=" * 60)
        receiver = input("📧 Recipient Email : ").strip()
        print("=" * 60)

        if receiver == "":

            speak("Recipient email cannot be empty.")

            return True

        speak("What is the subject?")

        subject = ""

        while subject == "":

            subject = listen()

        speak("What is the message?")

        body = ""

        while body == "":

            body = listen()

        print("\n" + "=" * 60)
        print("EMAIL PREVIEW")
        print("=" * 60)
        print(f"To      : {receiver}")
        print(f"Subject : {subject}")
        print(f"Message : {body}")
        print("=" * 60)

        speak("Do you want me to send this email? Say yes or no.")

        confirmation = ""

        for _ in range(3):

            confirmation = listen()

            if confirmation != "":
                break

            speak("I didn't catch that. Please say yes or no.")

        if confirmation == "":

            speak("No confirmation received. Email cancelled.")

            return True

        confirmation = confirmation.lower()

        if any(word in confirmation for word in [
            "yes",
            "yeah",
            "yup",
            "ok",
            "okay",
            "sure",
            "send",
            "send it"
        ]):

            speak("Sending your email.")

            success = send_email(
                receiver,
                subject,
                body
            )

            if success:

                speak("Email sent successfully.")

            else:

                speak("Sorry. I couldn't send your email.")

        else:

            speak("Email cancelled.")

    # ==========================================
    # Exit
    # ==========================================

    elif intent == "EXIT":

        speak("Goodbye Nikijon. Have a wonderful day.")

        return False

    # ==========================================
    # AI / Custom Commands
    # ==========================================

    else:

        # ---------- Custom Commands ----------

        if execute_custom_command(command):

            return True

        # ---------- Ignore Empty ----------

        if command.strip() == "":

            return True

        # ---------- Incomplete Commands ----------

        blocked_commands = [

            "who is",
            "what is",
            "tell me about",
            "define",
            "explain",
            "email",
            "mail",
            "send",
            "weather",
            "remind"

        ]

        if command.strip() in blocked_commands:

            speak("Please complete your request.")

            return True

        # ---------- Very Short Commands ----------

        if len(command.split()) <= 2:

            speak("Could you please be a little more specific?")

            return True

        # ---------- Gemini AI ----------

        print("\n🤖 MAX")
        print("🧠 Thinking...")

        answer = ask_ai(command)

        speak(answer)

    return True