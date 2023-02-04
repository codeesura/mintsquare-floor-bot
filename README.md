
# StarkNet Bot for Discord


This is a Discord bot for StarkNet blockchain built using Discord API and Web3.py. It updates the bot's nickname in every Discord server it's in to the current floor price of the specified token in the API call (0x01c7607659020c0f128fe677a1d7be9c3b9f66cedfe50296aca146b003875ee5). The price is updated every 15 seconds.

# Getting Started

To run this bot, you need to have a Discord API token and run the code in a Python environment.

## Prerequisites

- Python 3.6+
- Discord API token
- `discord.py` library. 
```Python
pip install discord.py
```
- `requests` library
```Python
pip install requests
```
- `web3` library
```Python
pip install web3
```
- `json` library
- `asyncio` library
- `time` library
- `datetime` library

## Installing

1. Install Python 3.6+ and set up a virtual environment.
2. Install the necessary libraries by running pip install discord.py requests json asyncio time datetime web3 in the terminal or command prompt.
3. Replace "TOKEN" in the code with your Discord API token.
4. Run the code in a Python environment.

## Features

- Updates bot's nickname in every Discord server to the current floor price of the specified token.
- Provides server information with the $server_info command.

## Built With

[Discord API ](#https://discord.com/developers/docs/intro)- The API used to build the bot

[Web3.py ](#https://web3py.readthedocs.io/en/stable/)- Ethereum API for Python

## Contributing

Feel free to contribute to the development of this bot by submitting pull requests or reporting issues.
