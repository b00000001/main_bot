import discord
import os

from discord.ext import commands
from cogs.utils import checks

#description showed when you use the help command
description = "test"

#sets up the bots characteristics. 
#command_prefix is the character used before commands
help_attrs = dict(hidden=True)
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description=description, pm_help=None, help_attrs=help_attrs)
                   
#a quick thing i made to look in a cogs folder and save all extensions in the list
def list_cogs():
    return ["cogs." + i.replace("/", "\\").split("\\")[0].replace(".py", "")
        for i in os.listdir("cogs") if i.endswith(".py")]

def load_cog(cog):
    try:
        bot.load_extension(cog)
        print('Loaded {}'.format(cog))
    except Exception as e:
        print('Failed to load cog {}\n{}: {}'.format(
            cog, type(e).__name__, e))

@bot.command(name="exit")
async def exit():
    await bot.logout()
 
#event for when the bot starts
@bot.event
async def on_ready():
    print('------')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------')

    #this can load the cogs/extensions
    for cog in list_cogs():
        load_cog(extension)

@bot.event
#whenever someone puts a message
async def on_message(message):
  await bot.process_commands(message)

@bot.event
#this runs when someone runs a command
async def on_command(command, ctx):

    message = ctx.message
    destination = None
    if message.channel.is_private:
        destination = 'Private Message'
    else:
        destination = '#{0.channel.name} ({0.server.name})'.format(message)



@bot.command(hidden=True)
@checks.is_owner()
async def load(cog : str):
    if "cogs." not in cog:
        cog = "cogs." + cog
    if not cog in list_cogs():
        await bot.say("The cog '{}' could not be found.".format(cog))
        return
    load_cog(cog)
    await bot.say("Loaded: {}".format(cog))

@bot.command(hidden=True)
@checks.is_owner()
async def unload(cog : str):
    if "cogs." not in cog:
        cog = "cogs." + cog
    if not cog in list_cogs():
        await bot.say("The cog '{}' could not be found.".format(cog))
        return
    bot.unload_extension(cog)
    await bot.say("Unloaded: {}".format(cog))

@bot.command(hidden=True)
@checks.is_owner()
async def reload(cog : str):
    if "cogs." not in cog:
        cog = "cogs." + cog
    if not cog in list_cogs():
        await bot.say("The cog '{}' could not be found.".format(cog))
        return
    bot.unload_extension(cog)
    load_cog(cog)
    await bot.say("Reloaded: {}".format(cog))

bot.run(email, password)
