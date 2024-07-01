# Discord Bot ChloéV2

This Discord bot is a Python project that enables a Discord bot to respond to user messages based on matches stored in an SQLite database. Users can teach the bot new responses using the `&learn` command followed by a key phrase and a response. The bot can also save the database under a specified name with the `&save` command.

## Main Features:
- Teach the bot new responses using the `&learn` command.
- Respond to user messages based on matches stored in the database.
- Save the database under a specified name with the `&save` command.

## Requirements:
- Python 3.x installed.
- Python modules `discord.py` and `sqlite3`.

## Installation and Configuration:
1. Clone this repository.
2. Install the required dependencies by running `pip install discord.py` in your terminal.
3. Create a Discord bot on the [Discord Developer Portal](https://discord.com/developers/applications).
4. Copy the bot token and replace `"BOT_TOKEN"` in the bot's code with this token.
5. Run the bot using the command `python bot.py` in the terminal.

## Usage:
- To add a new key, use the command `&learn KEY_PHRASE=RESPONSE_PHRASE`.
- To query the bot using a key phrase, simply type the key phrase in the chat.

Feel free to customize this bot to suit your needs. Have fun!
