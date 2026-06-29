def detect_intent(command):

    command = command.lower().strip()

    words = command.split()

    # ==========================================
    # Greeting
    # ==========================================

    if any(word in words for word in [
        "hello",
        "hi",
        "hey"
    ]):
        return "GREETING"

    # ==========================================
    # Open Applications / Websites
    # ==========================================

    elif any(word in command for word in [
        "open",
        "launch",
        "start"
    ]):
        return "OPEN"

    # ==========================================
    # Email
    # ==========================================

    elif any(word in command for word in [
        "send email",
        "send an email",
        "send mail",
        "email",
        "mail"
    ]):
        return "EMAIL"

    # ==========================================
    # Reminder
    # ==========================================

    elif any(word in command for word in [
        "remind",
        "reminder"
    ]):
        return "REMINDER"

    # ==========================================
    # Weather
    # ==========================================

    elif "weather" in command:
        return "WEATHER"

    # ==========================================
    # Google Search
    # ==========================================

    elif any(word in words for word in [
        "search",
        "google",
        "find",
        "lookup",
        "look"
    ]):
        return "SEARCH"

    # ==========================================
    # Time
    # ==========================================

    elif any(word in words for word in [
        "time",
        "clock"
    ]):
        return "TIME"

    # ==========================================
    # Date
    # ==========================================

    elif any(word in words for word in [
        "date",
        "day",
        "today"
    ]):
        return "DATE"

    # ==========================================
    # Exit
    # ==========================================

    elif any(word in words for word in [
        "bye",
        "goodbye",
        "exit",
        "quit",
        "stop",
        "shutdown"
    ]):
        return "EXIT"

    # ==========================================
    # AI
    # ==========================================

    return "AI"