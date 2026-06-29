import threading
import time

from modules.speech import speak


def reminder_task(seconds, message):

    time.sleep(seconds)

    print("\n" + "=" * 50)
    print("🔔 REMINDER")
    print("=" * 50)

    speak(f"This is your reminder. {message}")


def set_reminder(seconds, message):

    thread = threading.Thread(
        target=reminder_task,
        args=(seconds, message),
        daemon=True
    )

    thread.start()

    speak(f"Okay. I'll remind you in {seconds} seconds.")