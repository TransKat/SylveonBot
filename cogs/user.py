import discord
from discord.ext import commands
import random

sylveCount = 41

class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None\


    @commands.command(brief="Shows you a picture of Sylveon", aliases=["sylveon"])
    async def sylve(self, ctx):
        pic = random.randint(1, sylveCount)
        await ctx.send(f"Sylveon #{pic}")
        await ctx.send(f'http://web.freshmandevs.pw/files/sylveon/{pic}.png')

    @commands.command(brief="You can select an image of Sylveon, 1-88.")
    async def selectsylve(self, ctx, sylveon: int):
        pic = sylveon
        if sylveon > sylveCount:
            await ctx.send(f"Sorry, there are only {sylveCount} images available.")
        else:
            await ctx.send(f"Sylveon #{pic}")
            await ctx.send(f'http://web.freshmandevs.pw/files/sylveon/{pic}.png')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! That took {(round(self.bot.latency*1000, 1))}ms')


def setup(bot):
    bot.add_cog(User(bot))
