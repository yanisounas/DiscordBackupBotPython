if __name__ == "__main__":
    import os

    from dotenv import load_dotenv
    load_dotenv()

    from Bot.Core import core
    from Bot import load_bot

    bot = core.bot
    bot.run(os.getenv("BOT_TOKEN"))
