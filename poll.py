import discord
from discord.ext import commands
import asyncio

class Poll:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, polltimeinminutes: int): # Example: !poll 10
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
        options = {"🇦": "Option 1", # You can replace these options with variables and add them to the command.
                   "🇧": "Option 2",
                   "🇨": "Option 3"} # You can increase the option without any problems

        vote = discord.Embed(title="a", description="b", color=discord.Colour.blue()) # The poll embed, description can be None
        value = "\n".join("- {} {}".format(*item) for item in options.items()) # Add the options to the embed
        vote.add_field(name="c", value=value, inline=True) # c could be: Please vote ... :
        vote.set_footer(text="Time to vote: %s minutes" % (polltimeinminutes)) # You can delete this line if you want.

        message_1 = await ctx.send(embed=vote) # Send the vote embed in the channel. Use await self.bot.get_guild(snowflake).get_channel(snowflake).send(embed=vote)
                                               # A snowflake is 529552176626815391 for example. get_guild(server id), get_channel(channel id)
        for choice in options:
            await message_1.add_reaction(emoji=choice) # Add the reactions to the embed

        polltimeinminutes *= 60 # Multiply the polltimeinminutes with 60, because asyncio.sleep() has seconds as an argument
        await asyncio.sleep(polltimeinminutes) # Waits until the poll is over.
        message_1 = await ctx.get_message(message_1.id) # Get the message id to be able to see the reactions.

        counts = {react.emoji: react.count for react in message_1.reactions} # Counts the reactions
        winner = max(options, key=counts.get) # Gets the winner (Reactions with the highest votes)

        await ctx.send("**%s** has won!" % (options[winner])) # Winner message, you can use an embed here aswell for a better design or edit the vote embed.

def setup(bot):
    bot.add_cog(Poll(bot))