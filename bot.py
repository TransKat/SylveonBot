# Based on Hallucinate 21.05


import discord
import os
import json
from discord.ext import commands

version = "sylvebot 21.09.04 - my prefix is !, s!, or s."

# loads the token from token.txt

#with open('./token.txt') as f:
    #TOKEN = f.read()

# loads the token from config.json
TOKEN = json.load(open('config.json')).get('TOKEN')

client = commands.Bot(command_prefix=["!", "s!", "s.", "s$"], case_insensitive=True)


class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.blurple(), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)


client.help_command = MyHelpCommand()


@client.event
async def on_ready():
    print('Bot is online.')
    activity = discord.Game(name=f"{version}", type=0)
    await client.change_presence(status=discord.Status.online, activity=activity)
    return

# discord.py error handler


@client.event
async def on_command_error(ctx, error):
    await ctx.reply(error)
    print(f"Error caused by {ctx.author}. {error}")
    await ctx.message.add_reaction("❌")


@client.command(hidden=True)
@commands.is_owner()
async def setversion(ctx, *, arg,):
    global version
    version = arg
    await ctx.send(f"The version has been set to {arg}")
    activity = discord.Game(name=f"{arg}", type=0)
    await client.change_presence(status=discord.Status.online, activity=activity)
    await ctx.message.add_reaction("✅")


@client.command(hidden=True)
@commands.is_owner()
async def setstatus(ctx, *, arg):
    activity = discord.Game(name=f"{arg}", type=0)
    await client.change_presence(status=discord.Status.online, activity=activity)
    await ctx.send(f"You changed the bot's status to: Playing **{arg}**")
    await ctx.message.add_reaction("✅")


@client.command(hidden=True)
@commands.is_owner()
async def leave(ctx):
    await ctx.send(f"The bot is now leaving {ctx.guild.name}")
    await ctx.guild.leave()
    await ctx.message.add_reaction("✅")


@client.command(hidden=True)
@commands.is_owner()
async def ownersay(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)


@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Cog {extension} loaded")
    await ctx.message.add_reaction("✅")


@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Cog {extension} unloaded")
    await ctx.message.add_reaction("✅")


@client.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Cog {extension} has been reloaded.")
    await ctx.message.add_reaction("✅")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.command(hidden=True, name="guilds")
@commands.is_owner()
async def guild(ctx):
    await ctx.send(f"{client.guilds}\n")


@client.command(hidden=True)
@commands.is_owner()
async def eval(ctx, *, arg):
    exec(arg)
    await ctx.message.add_reaction("✅")


@client.command(hidden=True)
@commands.is_owner()
async def get_resource(ctx, arg):
    if arg == "token.txt":
        await ctx.send("You've been denied access to this file.")
        await ctx.message.add_reaction("❌")
    else:    
        await ctx.channel.send(file=discord.File(arg))
        print(f"Successfully gathered and uploaded {arg}.")
        await ctx.message.add_reaction("✅")


client.run(TOKEN)
