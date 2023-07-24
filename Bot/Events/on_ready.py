import os

from Bot.Core import core
from CLI import *

bot = core.bot


@bot.event
async def on_ready():
    cprint(f"""Discord Backup bot %G%ON%END%
=========== Bot ================
%B%Username%END%: {bot.user}
%B%ID%END%: {bot.user.id}
%B%Mode%END%: {os.getenv("MODE")}
=========== Servers ================
%B%Number%END%: {len(bot.guilds)}
""")
