import os
import subprocess
import webbrowser

from modules.speech import speak


def open_application(command):

    command = command.lower()

    apps = {

        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

        "vs code": r"C:\Users\KIIT\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code",

        "notepad": "notepad",

        "calculator": "calc",

        "paint": "mspaint",

        "command prompt": "cmd",

        "terminal": "cmd",

        "powershell": "powershell",

        "file explorer": "explorer",

        "explorer": "explorer",

        "camera": "start microsoft.windows.camera:",

        "spotify": r"C:\Users\KIIT\AppData\Roaming\Spotify\Spotify.exe"

    }

    for app, path in apps.items():

        if app in command:

            speak(f"Opening {app}")

            try:

                if path.startswith("http"):

                    webbrowser.open(path)

                elif path.startswith("start"):

                    os.system(path)

                else:

                    subprocess.Popen(path)

            except Exception:

                speak(f"Unable to open {app}")

            return True

    return False