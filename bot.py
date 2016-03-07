import discord
import os

from discord.ext import commands

#description showed when you use the help command
description = "test"

#sets up the bots characteristics. 
#command_prefix is the character used before commands
help_attrs = dict(hidden=True)
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description=description, pm_help=None, help_attrs=help_attrs)
                   
#a quick thing i made to look in a cogs folder and save all extensions in the list
extensions = ["cogs." + i.replace("/", "\\").split("\\")[0].replace(".py", "")
              for i in os.listdir("cogs") if i.endswith(".py")]
   
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
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(
                extension, type(e).__name__, e))

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

    

bot.run(email, password)

