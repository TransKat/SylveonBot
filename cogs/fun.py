import discord
import random
import time
import json
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief="Generates a random number from 0 to a number of your choice.")
    async def gennumber(self, ctx, arg):
        output = random.randint(0, (int(arg)))
        await ctx.reply(output)

    @commands.command(brief="Generates a random number from 0 to 5000")
    async def random(self, ctx):
        num = random.randrange(0, 5000)
        await ctx.reply(f"{ctx.author.mention}, the result was {num}")
        await ctx.message.add_reaction("✅")

    @commands.command(brief="Have fun dying.")
    async def die(self, ctx):
        value = random.randint(0, 14)
        await ctx.send(json.load(open('response-die.json')).get(f'{value}'))
        await ctx.send(json.load(open('die-rhetorical.json')).get(f'{value}'))

    @commands.command(brief="murder each other!")
    async def kill(self, ctx, member:discord.User):
        value = random.randint(0, 14)
        if value == 0:
            await ctx.send(f"<@{ctx.author.id}> pushed <@{member.id}> into lava")
        elif value == 1:
            await ctx.send(f"<@{ctx.author.id}> tweeted cringe but <@{member.id}> saw it and died of cringe")
        elif value == 2:
            await ctx.send(f"<@{ctx.author.id}> stabbed @<{member.id}")
        elif value == 3:
            await ctx.send(f"<@{ctx.author.id}> \"accidentally\" shot <@{member.id}>")
        elif value == 4:
            await ctx.send(f"<@{ctx.author.id}> poisoned <@{member.id}>\'s food")
        elif value == 5:
            await ctx.send(f"<@{ctx.author.id}> removed <@{member.id}>\'s lungs")
        elif value == 6:
            await ctx.send(f"<@{ctx.author.id}> sent <@{member.id}> a bomb in the mail")
        elif value == 7:
            await ctx.send(f"<@{ctx.author.id}> got <@{member.id}> so drunk they fell off a building and didn't bounce")
        elif value == 8:
            await ctx.send(f"<@{ctx.author.id}> had too much drip and <@{member.id}> died of jealousy")
        elif value == 9:
            await ctx.send(f"<@{ctx.author.id}> stole <@{member.id}>\'s fridge and they starved")
        elif value == 10:
            await ctx.send(f"<@{member.id}> disrespected Sylveon and was murdered by <@{ctx.author.id}>")
            await ctx.send("This... does put a smile on my face.")
        elif value == 11:
            await ctx.send(f"<@{ctx.author.id}> deleted <@{member.id}> with the power of Sylveon")
        elif value == 12:
            await ctx.send(f"<@{member.id}> ordered a sylveon plush online but <@{ctx.author.id}> swapped it with anthrax")
        else:
            await ctx.send(f"<@{ctx.author.id}> murdered <@{member.id}> in some horrific way unexplainable on Discord")


def setup(client):
    client.add_cog(Fun(client))
