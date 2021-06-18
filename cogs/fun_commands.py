import discord
import json
import random
from discord.ext import commands


print("Initializing Fun commands")
with open("variables.json", "r") as var_able:
    variables = json.load(var_able)


class Fun(commands.Cog):
    """
    A class for all the fun commands
    """
    def __init__(self, client):
        self.client = client

    # @commands.Cog.listener() for event
    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f"pong! {round(self.client.latency * 1000)}ms", mention_author=False)

    @commands.command()
    async def pp(self, ctx, member=None):
        # Uses value ranging from 0 - 15
        if member is None:
            pp_size = random.randint(0, 15) * '='
            pp_embed = discord.Embed(title="pp size machine", description=f"{ctx.author.mention}'s penis\n" +
                                                                          "8" + pp_size + "D", colour=0xFFAAFF)
            await ctx.send(embed=pp_embed)

        else:
            pp_size = random.randint(0, 15) * '='
            pp_embed = discord.Embed(title="pp size machine", description=f"{member}'s penis\n" + "8" + pp_size + "D",
                                     colour=0xFFAAFF)

            await ctx.send(embed=pp_embed)

    @commands.command(aliases=["simp", "sr"])
    async def simprate(self, ctx, member=None):
        # Uses random integer B/W 0-100
        if member is None:
            sim = discord.Embed(title="simp r8 machine", description=f"{ctx.author.mention}"
                                                                     f" is {random.randint(0, 100)}% simp ",
                                color=0xAACCFF)
            await ctx.send(embed=sim)
        else:
            sim = discord.Embed(title="simp r8 machine", description=f"{member} is {random.randint(0, 100)}% simp ",
                                color=0xAACCFF)
            await ctx.send(embed=sim)

    @commands.command(aliases=["gay", "gr"])
    async def gayrate(self, ctx, member=None):
        # Uses random integer B/W 0-100
        if member is None:
            gayeee = discord.Embed(title="gay r8 machine",
                                   description=f"{ctx.author.mention} is {random.randint(0, 100)}% gay :rainbow_flag:",
                                   color=0xFFCCAA)
            await ctx.send(embed=gayeee)
        else:
            gayeee = discord.Embed(title="gay r8 machine",
                                   description=f"{member} is {random.randint(0, 100)}% gay :rainbow"
                                               f"_flag:", color=0xFFCCAA)
            await ctx.send(embed=gayeee)

    @commands.command(aliases=["8ball", "ask"])
    async def ball_eight(self, ctx, *, question):
        """
        This command was a quite tuff, there are some problems init, this checks the whole question and finds words like
        'who', 'which'... etc and if found none, it replies in yes or no
        """
        i = 0
        j = question.split(" ")
        for wod in j:
            if wod.upper() == "MANY":
                i = 1
            if wod.upper() == "WHY":
                i = 2
            if wod.upper() == "WHO":
                i = 3
        if i == 0:
            # If no "wh" questions found
            eight_ball = ["YES",  # Y
                          "It is decidedly so.",
                          "It is certain.",
                          "Without a doubt.",
                          "Yes - definitely.",
                          "You may rely on it.",
                          "As I see it, yes.",
                          "Most likely.",
                          "Outlook good.",
                          "Nope, ||Sike thats the wrong answer||",
                          "Your mom said yes.",
                          "Signs point to yes.",
                          "NANI?",  # D
                          "Can't answer RN, busy with your sista.",
                          "Can't answer RN, your mom ain't letting me go.",
                          "Better not ask.",
                          "Cannot predict now.",
                          "Better not tell you know.",
                          "Outlook not so good.",
                          "NO.",  # N
                          "Your dad said no",
                          "Was there ever a doubt?",
                          "Points towards NO",
                          "My reply is no.",
                          "Yes, ||Sike NOPE||",
                          "My sources say no.",
                          "OH HELL NAH"]
            await ctx.channel.send(f"**Question:** {question}\n**Answer:** {random.choice(eight_ball)}")
        elif i == 1:
            # If the questions contains the word "many"
            await ctx.channel.send(f"**Question:** {question}\n**Answer:** {random.randint(-5, 20)}")
        elif i == 2:
            # If the questions contains the word "why"
            eight_ball = [
                "umm idk",
                "go ask your mom, ||OH WAIT SHE DED||",
                "GO ask yo dad nigga, ||oh wait he dead||",
                "coz you are gay",
                "coz you love trump",
                ""
            ]
            await ctx.channel.send(f"**Question:** {question}\n**Answer:** {random.choice(eight_ball)}")
        elif i == 3:
            # If the questions contains the word "who"
            eight_ball = [
                "TRUMP!",
                "Hitler",
                "your mom",
                "your fat ass mom nigga",
                "your uncle",
                "QUEEN ELIZABETH",
                "DONALD J TRUMP",
                "PUTIN",
                "a jewww",
                "NIGGA",
                "That guy with a smol dick"
            ]
            await ctx.channel.send(f"**Question:** {question}\n**Answer:** {random.choice(eight_ball)}")

    @ball_eight.error
    async def ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            ball_handle_errors = ["Understandable, have a nice day",
                                  "Maybe I am blind, can't see the question",
                                  "Aayo wait, Your mom stole my glasses\nI can't see the question",
                                  "Question where",
                                  "Why are you gay?"]
            await ctx.reply(f"{random.choice(ball_handle_errors)}", mention_author=False)

    @commands.command(aliases=["pfp"])
    async def profile(self, ctx, user: discord.Member = None):
        """
        Still needs to improve this command a little bit, it returns some basic user data
        """
        if user is None:
            user = ctx.author
        em = discord.Embed(title=f"{user}", colour=user.color)
        j = user.joined_at
        em.add_field(name="Joined at", value=f"{j.day} {variables['mon'][str(j.month)]} "
                                             f"{j.year}, {j.hour}:{j.minute}:{j.second} UTC")
        em.add_field(name="Top Role", value=f"{user.top_role}")
        em.add_field(name="Guild perms", value=f"{user.guild_permissions}")
        em.set_image(url=user.avatar_url)
        await ctx.channel.send(embed=em)


def setup(client):
    client.add_cog(Fun(client))
