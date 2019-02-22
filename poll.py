import discord
from discord.ext import commands
import asyncio

class Poll:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="poll", aliases=["vote"])
    async def poll(self, ctx, polltimeinminutes: int, headline:str="Poll", *, description:str="Click"):
        """simple poll command"""
        # example: p.poll 10
        # headline and description
        """
        A poll command for a Discord bot.

        Design: https://gyazo.com/d9ad1e56c0cfae2c8350f5bb173da16b

        Discord.py rewrite version: 1.0.0a
        Python version: 3.7.1

        Made by PhosphorTV
        Socials:
        • Discord: PhosphorTV#0995
        • Twitter: @PhosphorTV_TTV
        • Twitch: PhosphorTV_

        DM me on Discord if you need help
        Be sure to join my Discord Bot testing server: discord.gg/KcRpSFa
        """
        opt1 = "A"
        opt2 = "B"
        opt3 = "C"
        options = {"🇦": opt1, # You can replace these options with variables and add them to the command.
                   "🇧": opt2,
                   "🇨": opt3} # You can increase the option without any problems

        vote = discord.Embed(title=headline, description=description, color=discord.Colour.blue()) # The poll embed, description can be None
        value = "\n".join("- {} {}".format(*item) for item in options.items()) # Add the options to the embed
        vote.add_field(name="Click:", value=value, inline=True) # c could be: Please vote ... :
        vote.set_footer(text="Time to vote: %s minutes" % (polltimeinminutes)) # You can delete this line if you want.

        message_1 = await ctx.send(embed=vote) # Send the vote embed in the channel. Use await self.bot.get_guild(snowflake).get_channel(snowflake).send(embed=vote)
                                               # A snowflake is 529552176626815391 for example. get_guild(server id), get_channel(channel id)
        for choice in options:
            await message_1.add_reaction(emoji=choice) # Add the reactions to the embed

        polltimeinminutes *= 60 # Multiply the polltimeinminutes with 60, because asyncio.sleep() has seconds as an argument
        await asyncio.sleep(polltimeinminutes) # Waits until the poll is over.
        message_1 = await ctx.get_message(message_1.id) # Get the message id to be able to see the reactions.

        counts = {react.emoji: react.count for react in message_1.reactions} # Counts the reactions
        if counts["🇦"] == 1 and counts["🇧"] == 1 and counts["🇨"] == 1: # if nobody reacts, the bot will send a info message
            raise commands.CommandInvokeError
        else:
            winner = max(options, key=counts.get) # Gets the winner (Reactions with the highest votes)

            await ctx.send("**%s** has won!" % (options[winner])) # Winner message, you can use an embed here aswell for a better design or edit the vote embed.

    @poll.error
    async def on_error(self, ctx, error):
        RED = discord.Colour.red()
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Sorry, you missed an argument", description="You forgot the 'time to vote time'\n"f"`p.poll 10` - 10 minutes vote time!", color=RED)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            print("I dont have permissions!")
            print(error)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(title="Oh, dude!", description="This isn't a time - time is a **number** ~ e.g `1`", color=RED)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(title="Vote canceled, because nobody votes!", color=RED)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Poll(bot))
