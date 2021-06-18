import discord
from discord.ext import commands, tasks
from itertools import cycle
import json

print("Initializing events")
with open("variables.json", "r") as var_able:
    variables = json.load(var_able)


class BotEvents(commands.Cog):
    """
    A class for all the 'events' performed by the bot
    """
    def __init__(self, client):
        @client.event
        async def on_ready():
            with open("variables.json", "w") as f:
                variables['version'] += 0.01
                json.dump(variables, f, indent=2)
            print(f"\n\nBot is ready\nversion: {variables['version']}")
            change_status.start()

        @tasks.loop(seconds=variables['status_change_time'])
        @client.event
        async def change_status():
            await client.change_presence(status=discord.Status.online,
                                         activity=discord.Game(next(cycle(variables['status']))))

        @client.event
        async def on_command_error(ctx, error):
            if isinstance(error, commands.CommandNotFound):
                await ctx.reply("No command found\nTry typing `Dad help`", mention_author=False)


def setup(client):
    client.add_cog(BotEvents(client))
