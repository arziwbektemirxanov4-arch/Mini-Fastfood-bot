# Configuration settings for the Fastdood Telegram bot

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = "https://api.telegram.org/bot" + BOT_TOKEN
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID", None)

# Additional configuration settings can be added here as needed.