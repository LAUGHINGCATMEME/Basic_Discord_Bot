import discord
from discord.ext import commands
import json
import os


print(f"Discord version: {discord.__version__}")
with open("variables.json", "r") as var_able:
    variables = json.load(var_able)

client = commands.Bot(command_prefix=variables['prefix'])

for filename in os.listdir("./cogs"):
    """
    Loads all the python files in the cogs folder
    """
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

if __name__ == "__main__":
    """
    Starts the bot
    """
    client.run(variables["token"])
