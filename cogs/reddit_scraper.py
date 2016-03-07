#imports discord and the cog library
import discord, asyncio
from discord.ext import commands
from .utils import checks, scraper



#this is the cog / extension
class RedditScraper:

    def __init__(self, bot : commands.Bot):
        self.bot = bot

    #hidden = True means that when you do [command bang] help it won't show
    # @commands.command(hidden=True)
    # async def test(self, *message):
    #     await self.bot.say(" ".join(message))

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
                # i = 0
                # for post in result:
                #     await self.bot.say(post) if i == 0 else await self.bot.say('\n' + post)
                #     asyncio.sleep(1)
                await self.bot.say("\n\n".join(result))
            else:
                await self.bot.pm_help(ctx)

    # #pass_context will pass on the message info of the person who called the command
    # #ctx is needed for the pass_context
    # #num is a sub-command thing like !clearbot 29
    # @commands.command(pass_context=True)
    # async def clearbot(self, ctx, num: int):
    #     count = 0
    #     if num < 0:
    #         return
    #
    #     while count <= num:
    #         del_flag = False
    #         async for msg in self.bot.logs_from(ctx.message.channel, limit=100):
    #             if count == num:
    #                 break
    #             elif msg.author.id == self.bot.user.id:
    #                 count += 1
    #                 del_flag = True
    #                 await self.bot.delete_message(msg)
    #
    #         if not del_flag:
    #             break


#for the bot to add the cog. replace template with the classname
def setup(bot):
    bot.add_cog(RedditScraper(bot))