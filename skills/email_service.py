import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def send_email(receiver, subject, body):

    try:

        msg = EmailMessage()

        msg["Subject"] = subject
        msg["From"] = EMAIL
        msg["To"] = receiver

        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(EMAIL, PASSWORD)

            smtp.send_message(msg)

        return True

    except Exception as e:

        print("Email Error:", e)

        return False