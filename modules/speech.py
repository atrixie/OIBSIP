import time
import speech_recognition as sr
import pyttsx3

# ==========================================
# TEXT TO SPEECH
# ==========================================

engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 180)
engine.setProperty("volume", 1.0)


def speak(text):

    print(f"\n🤖 MAX : {text}")

    engine.say(text)
    engine.runAndWait()

    # Wait before opening microphone
    time.sleep(1)


# ==========================================
# SPEECH RECOGNITION
# ==========================================

recognizer = sr.Recognizer()

recognizer.energy_threshold = 250
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 1.8
recognizer.non_speaking_duration = 0.8


def listen():

    with sr.Microphone() as source:

        print("\n🎤 Listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        try:

            audio = recognizer.listen(

                source,

                timeout=10,

                phrase_time_limit=20

            )

        except sr.WaitTimeoutError:

            return ""

    try:

        print("🧠 Recognizing...")

        command = recognizer.recognize_google(

            audio,

            language="en-IN"

        )

        command = command.lower().strip()

        print(f"👤 You : {command}")

        return command

    except sr.UnknownValueError:

        print("⚠️ Didn't catch that.")

        return ""

    except sr.RequestError:

        print("❌ Speech service unavailable.")

        return ""

    except Exception as e:

        print(e)

        return ""