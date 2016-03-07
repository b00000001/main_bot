import discord
from discord.ext import commands
import datetime
import time
import aiohttp
import asyncio

""" Chat cog """
class Chat:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden= True)
    async def say(self, *text):     # !say text
        await self.bot.say(" ".join(text))

def setup(bot):
    bot.add_cog(Chat(bot))
