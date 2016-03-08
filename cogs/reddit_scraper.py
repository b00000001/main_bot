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
    async def get(self, ctx : commands.Context, subreddit, posts=5, category='hot'):
        """Base command for returning data from a subreddit.
        Keyword arguments:
        posts -- Number of posts to return (default 5)
        category -- Category to look at [hot, new, rising, controversial, top] (default hot)
        """
        if posts > 25:
            await self.bot.say('Number of posts must be no greater than 25.')
        else:
            if subreddit.lower().strip().__len__() > 0:
                if category in scraper.categories:
                    result = await scraper.getSubredditTop(self.bot.session, subreddit, posts, category)
                    await self.bot.say("\n\n".join(result))
                else:
                    await self.bot.say('Category must be valid: ' + ", ".join(scraper.categories))
            else:
                await self.bot.pm_help(ctx)


#for the bot to add the cog. replace template with the classname
class WundergroudScraper:

	def __init__(self, bot: commands.Bot):
		self.bot = bot
		
	@commands.group(name="weather", pass_conext=True)
	async def _weather(self, ctx):
	if ctx.invoked_subcommand is None:
		await self.bot.pm_help(ctx)
		
	@weather.command(pass_context=True, name="getforecast")
	async def getforecast(self, ctx : commands.Context, forecast):
		if forecast.lower() .strip() .__len__() > 0:
			result = await weatherscrap.together
			await self.bot.say(result)
		else: 
			await self.bot.pm_help(ctx)
		
def setup(bot):
    bot.add_cog(RedditScraper(bot))
	bot.add_cog(WundergroundScraper(bot))