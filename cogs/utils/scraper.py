import asyncio, json
from discord.ext import commands

async def getSubredditJSON(session, subreddit, category):
    return await getJSON(session, 'https://www.reddit.com/r/' + subreddit + '/' + category + '/.json')

async def getJSON(session, url):
    async with session.get(url) as resp:
        return await resp.json()

async def getPostFromJSON(postData : dict):
    post = postData['data']
    score = post['score']
    author = post['author']
    isNSFW = post['over_18']
    link = post['url']
    title = post['title']

    return '**Title:** {0}\n**Link:** <{1}>\n**Author:** {2}\n**Score:** {3}\n**NSFW:** {4}'.format(title, link, author, score, isNSFW)

async def getPosts(srPosts, num):
    posts = []
    i = 0
    for post in srPosts:
        if i >= num:
            break
        posts.append(await getPostFromJSON(post))
        i += 1

    return posts

async def getSubredditTop(session, subreddit, num, category='hot'):
    srData = await getSubredditJSON(session, subreddit, category)
    srPosts = srData['data']['children']

    return await getPosts(srPosts, num)

