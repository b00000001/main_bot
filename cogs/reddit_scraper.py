#imports discord and the cog library
import discord, asyncio
from discord.ext import commands
from .utils import checks, scraper

#this is the cog / extension
class RedditScraper:

    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.group(name="reddit", pass_context=True)
    @checks.is_owner()
    async def _reddit(self, ctx):
        """Useful commands for getting information from reddit."""
        if ctx.invoked_subcommand is None:
            await self.bot.pm_help(ctx)

    @_reddit.command(pass_context=True, name="get")
    async def get(self, ctx : commands.Context, subreddit, posts=5):
        """Base command for returning data from a subreddit."""
        if posts > 25:
            await self.bot.say('Number of posts must be no greater than 25.')
        else:
            if subreddit.lower().strip().__len__() > 0:
                result = await scraper.getSubredditTop(self.bot.session, subreddit, posts)
                await self.bot.say("\n\n".join(result))
            else:
                await self.bot.pm_help(ctx)


#for the bot to add the cog. replace template with the classname
def setup(bot):
    bot.add_cog(RedditScraper(bot))