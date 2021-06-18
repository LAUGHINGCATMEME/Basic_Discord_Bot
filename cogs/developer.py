from discord.ext import commands
import json

print("Initializing developer commands")
with open("variables.json", "r") as var_able:
    variables = json.load(var_able)


class Developer(commands.Cog):
    """
    A class for all the commands related to the developer
    """
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["ttd", "tothedev"])
    @commands.cooldown(1, 60)
    async def tothedeveloper(self, ctx):
        """
        Prints the message on the terminal
        :param ctx: Message
        :return:
        """
        print(f"from: {ctx.author}  message: {ctx.message.content}")
        await ctx.reply(f"Successfully sent your message to the developer", mention_author=False)


def setup(client):
    client.add_cog(Developer(client))
