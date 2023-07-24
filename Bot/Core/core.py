import discord
import os

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=os.getenv("BOT_PREFIX"),
    intents=intents,
    description=os.getenv("BOT_DESCRIPTION"),
    help_command=None)


class BaseHelp:
    def __init__(self):
        self.command_infos = {}

    def __getattr__(self, value):
        try:
            return self.command_infos[value]
        except KeyError:
            return None


class BaseError(Exception):
    pass
