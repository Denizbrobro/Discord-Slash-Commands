# Discord-Slash-Commands
Using Python.
Created By: Denizbrobro

## Installation

To set up the Discord.py interaction features, use the **[pip](https://pip.pypa.io/en/stable/)** package manager and execute the following command:

```bash
pip install discord
pip install discord-py-interactions
```

## Discord.py Interaction Guide

The Discord.py library is a powerful tool for creating Discord bots in the Python language. This guide provides a fundamental understanding for developers looking to incorporate interactive commands (slash commands) and button interactions into their Discord servers.

### Types of Interactions

There are two main types of interactions used in Discord.py:

1. **Slash Commands:** Allows users to execute commands starting with a forward slash (/). For example, "/command".

2. **Button Interactions:** Enables users to click on buttons, providing your bot with more control and interaction options.

### How to Use

1. Add your bot to the Discord server.
2. Secure your bot's token.
3. Integrate the interaction module into your bot's main file:

```python
import discord
from discord.ext import commands
from discord.interactions import Interaction
```

## License

This project is licensed under the **[MIT License](https://choosealicense.com/licenses/mit/)**.
