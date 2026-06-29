import datetime

from modules.speech import speak


def tell_time():

    current = datetime.datetime.now().strftime("%I:%M %p")

    speak(f"The current time is {current}")


def tell_date():

    today = datetime.datetime.now().strftime("%d %B %Y")

    speak(f"Today is {today}")