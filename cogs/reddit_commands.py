import discord
from discord.ext import commands
import random
import praw
import json


print("Installing memes")
with open("variables.json", "r") as var_able:
    variables = json.load(var_able)

if variables['reddit_variables'] is True:
    meme_list = ["memes", "cursedmemes", "dankmemes"]
    reddit = praw.Reddit(client_id=variables["reddit_variables"]["client_id"],
                         client_secret=variables["reddit_variables"]["client_secret"],
                         username=variables["reddit_variables"]["username"],
                         password=variables["reddit_variables"]["password"],
                         user_agent=variables["reddit_variables"]["user_agent"])

    lst_of_sub_inr = []
    ass_list = []
    for i in meme_list:
        tops = reddit.subreddit(i).top(limit=variables["reddit_variables"]["meme_download_limit"])
        for submission in tops:
            lst_of_sub_inr.append(submission)
    print("Installing ass")
    ass = reddit.subreddit("ass").top(limit=200)
    for i in ass:
        ass_list.append(i)


    class Red(commands.Cog):
        """
        You'll need to put all the variables in 'reddit_variables' in variables.json or else it'll give an error
        """
        def __init__(self, client):
            self.client = client

        @commands.command()
        async def meme(self, ctx):
            """
            The amount of memes which are downloaded form each sun is determined by
            variables["reddit_variables"]["meme_download_limit"] from the subs r/memes, r/cursedmemes, r/dankmemes
            :param ctx: Message
            :return:
            """
            meme_sub = random.choice(lst_of_sub_inr)
            name_of_url = "https://www.reddit.com" + meme_sub.permalink
            em = discord.Embed(title=meme_sub.title, url=name_of_url, color=0x00FFFF)
            em.set_image(url=meme_sub.url)
            em.set_footer(text=f"{meme_sub.score} 👍  |  {meme_sub.num_comments} 💬")
            await ctx.reply(embed=em, mention_author=False)

        @commands.command()
        async def ass(self, ctx):
            """
            Uses any random of the top 200 posts in r/ass
            :param ctx: Message
            :return:
            """
            channel = discord.Client.get_channel(self.client, ctx.channel.id)
            if not channel.is_nsfw():
                await ctx.reply("BONK! use this command in nsfw channel :bonl:", mention_author=False)
                return
            ass_sub = random.choice(ass_list)
            name_of_url = "https://www.reddit.com" + ass_sub.permalink
            em = discord.Embed(title=ass_sub.title, url=name_of_url, color=0xFFFF00)
            em.set_image(url=ass_sub.url)
            em.set_footer(text=f"requested by {ctx.message.author}")
            await ctx.reply(embed=em, mention_author=False)


    def setup(client):
        client.add_cog(Red(client))
else:
    print("Reddit commands are disabled")


    class Meh(commands.Cog):
        def __init__(self, client):
            self.client = client


    def setup(client):
        client.add_cog(Meh(client))
