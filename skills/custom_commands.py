import json
import webbrowser
import os

from modules.speech import speak

CONFIG_FILE = "config.json"


def execute_custom_command(command):

    try:

        with open(CONFIG_FILE, "r") as file:

            commands = json.load(file)

    except Exception:

        speak("Unable to load custom commands.")

        return False

    command = command.lower()

    for key, value in commands.items():

        if key.lower() in command:

            speak(f"Opening {key}")

            if value.startswith("http"):

                webbrowser.open(value)

            else:

                if os.path.exists(value):

                    os.startfile(value)

                else:

                    speak("The file could not be found.")

            return True

    return False