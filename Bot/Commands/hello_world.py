from Bot.Core import core

bot = core.bot


class Help(core.BaseHelp):
    def __init__(self):
        super().__init__()
        self.command_infos = {
            'name': 'hello_world',
            'args': None,
            'desc': 'Basic Hello World'
        }


@bot.command()
async def hello_world(ctx):
    await ctx.send("Hello world")
