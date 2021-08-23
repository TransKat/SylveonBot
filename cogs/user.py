import discord
from discord.ext import commands
import random
from googlesearch import search


class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(brief="Says hello")
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

    @commands.command(brief="Shows you a picture of Sylveon", aliases=["sylveon"])
    async def sylve(self, ctx):
        pic = random.randint(1, 88)
        if pic == 6:
            await ctx.send(f"Sylveon #{pic}, Cosmo!")
        elif pic == 8:
            await ctx.send(f"Sylveon #{pic}, Sylvia!")
        elif pic == 10:
            await ctx.send(f"adorable! (#10)")
        elif pic == 37:
            await ctx.send(f"wheeeeee!!! (#37)")
        elif pic == 41:
            await ctx.send(f"they comin to whoop yo ass (#41)")
        else:
            await ctx.send(f"Sylveon #{pic}")
        await ctx.send(f'https://kat.is-coding-on-the.net/file/sylveon/{pic}.png')

    @commands.command(brief="You can select an image of Sylveon, 1-88.")
    async def selectsylve(self, ctx, sylveon: int):
        pic = sylveon
        if pic == 6:
            await ctx.send(f"Sylveon #{pic}, Cosmo!")
        elif pic == 8:
            await ctx.send(f"Sylveon #{pic}, Sylvia!")
        elif pic == 10:
            await ctx.send(f"adorable! (#10)")
        elif pic == 37:
            await ctx.send(f"wheeeeee!!! (#37)")
        elif pic == 41:
            await ctx.send(f"they comin to whoop yo ass (#41)")
        else:
            await ctx.send(f"Sylveon #{pic}")
        await ctx.send(f'https://kat.is-coding-on-the.net/file/sylveon/{pic}.png')

    @commands.command(brief="Shows you a gif of Sylveon", aliases=["sylveongif", "gif"])
    async def sylvegif(self, ctx):
        pic = random.randint(1, 6)
        # if pic == 6:
        #    await ctx.send(f"Sylveon #{pic}, Cosmo!")
        # elif pic == 8:
        #    await ctx.send(f"Sylveon #{pic}, Sylvia!")
        # elif pic == 10:
        #    await ctx.send(f"adorable! (#10)")
        # elif pic == 37:
        #    await ctx.send(f"wheeeeee!!! (#37)")
        # elif pic == 41:
        #    await ctx.send(f"they comin to whoop yo ass (#41)")
        # else:
        await ctx.send(f"Sylveon gif #{pic}")
        await ctx.send(f'https://kat.is-coding-on-the.net/file/sylveon/{pic}.gif')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! That took {(round(self.bot.latency*1000, 1))}ms')

    @commands.command(aliases=["google"])
    async def gsearch(self, ctx, *, arg):
        strarray = search(arg, num_results=10, lang="en")
        onestring = "\n".join(strarray)
        embed = discord.Embed(
            title=f'Showing results 1-10 for \"{arg}\".',
            description=onestring,
            colour=discord.Colour.green()

        )
        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(User(bot))
