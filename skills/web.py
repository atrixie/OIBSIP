import webbrowser

from modules.speech import speak
from skills.apps import open_application


def open_site(command):

    if open_application(command):

        return

    command = command.lower()

    websites = {

        "youtube": "https://youtube.com",

        "github": "https://github.com",

        "linkedin": "https://linkedin.com",

        "gmail": "https://mail.google.com",

        "chatgpt": "https://chat.openai.com",

        "spotify": "https://spotify.com",

        "instagram": "https://instagram.com"

    }

    for site, url in websites.items():

        if site in command:

            speak(f"Opening {site}")

            webbrowser.open(url)

            return

    speak("I couldn't find that application or website.")