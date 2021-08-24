import discord
from discord.ext import commands
import random
from googlesearch import search
import praw


reddit = praw.Reddit(client_id='your client id',
                     client_secret='your client secret',
                     user_agent='your user agent')


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

    @commands.command(brief="is it not obvious")
    async def meme(self, ctx):
        num = random.randint(0,2)
        if num == 0:
            sub = "196"
        elif num == 1:
            sub = "traaaaaaannnnnnnnnns"
        else:
            sub = "memes"
        memes_submissions = reddit.subreddit(sub).new()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await ctx.send(f"From r/{sub}")
        await ctx.send(submission.url)


def setup(bot):
    bot.add_cog(User(bot))
