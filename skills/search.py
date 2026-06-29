import urllib.parse
import webbrowser

from modules.speech import speak


def search(command):

    words = [
        "search",
        "google",
        "please",
        "find",
        "look up",
        "can you",
        "could you",
        "for"
    ]

    query = command.lower()

    for word in words:

        query = query.replace(word, "")

    query = query.strip()

    if query == "":

        speak("What should I search?")

        return

    speak(f"Searching Google for {query}")

    url = "https://www.google.com/search?q=" + urllib.parse.quote(query)

    webbrowser.open(url)