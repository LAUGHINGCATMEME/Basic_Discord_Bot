from discord.ext import commands
import json

print("Initializing moosic commands")
with open("variables.json", "r") as var_able:
    variables = json.load(var_able)


class Moosic(commands.Cog):
    """
    SOME ONE FUCKING HELP ME ON THIS ONE
    """
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(Moosic(client))
