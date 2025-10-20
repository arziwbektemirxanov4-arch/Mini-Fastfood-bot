def format_message(message: str) -> str:
    # Function to format messages before sending
    return message.strip().capitalize()

def log_message(message: str) -> None:
    # Function to log messages for debugging
    print(f"Log: {message}")