# Mini-Fastfood-bot

# Fastdood Telegram Bot

This project is a custom Telegram bot for Fastdood, designed to enhance user interaction and provide various functionalities.

## Project Structure

```
fastdood-telegram-bot
├── src
│   ├── bot.py               # Main entry point for the Telegram bot
│   ├── handlers             # Contains command handlers for the bot
│   │   └── __init__.py
│   ├── utils                # Utility functions for the bot
│   │   └── __init__.py
│   └── config.py           # Configuration settings for the bot
├── requirements.txt         # Lists dependencies required for the project
├── README.md                # Documentation for the project
└── .env                     # Stores environment variables
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fastdood-telegram-bot
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Create a `.env` file in the root directory and add your bot token:
   ```
   BOT_TOKEN=your_bot_token_here
   ```

## Usage

To run the bot, execute the following command:
```
python src/bot.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.
