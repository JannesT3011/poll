from discord.ext import commands

bot = commands.Bot(command_prefix="p.", description="A poll command for a discord bot")

TOKEN = "" # Insert your bot token

@bot.event
async def on_ready():
    print("=============\n""Logged in as\n"f"{bot.user.name}\n""=============")

if __name__ == '__main__':
    bot.load_extension("poll")
    bot.run(TOKEN)