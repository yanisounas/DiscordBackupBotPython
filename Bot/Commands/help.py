import discord
import os

from Bot.Core import core

from importlib import import_module

bot = core.bot


class Help(core.BaseHelp):
    def __init__(self):
        super().__init__()
        self.command_infos = {
            'name': 'help',
            'args': None,
            'desc': 'Show the help message'
        }


helps = {}
for file in os.listdir('Bot/Commands'):
    if file != "__init__.py" and file != "__pycache__" and not file.startswith('dev.'):
        try:
            helps[file[:-3]] = getattr(import_module(f'Bot.Commands.{file[:-3]}'), 'Help')()
        except AttributeError as e:
            print(f"WARNING: Generating help command for {file} Failed")
            print(f"Debug: {e}\n")
        except Exception as e:
            print(f"{file} Failed")
            print(f"Debug: {e}\n")


@bot.command(aliases=['h'])
async def help(context, command=None):
    msg = discord.Embed(title="", color=0xb71c1c)
    if not command:
        for h in helps.values():
            msg.add_field(name=h.name, value=h.desc, inline=False)
    else:
        try:
            msg.add_field(name=helps[command].name, value=helps[command].desc)
        except KeyError:
            msg.add_field(name='Error', value="Command not found", inline=False)
    await context.send(embed=msg)
