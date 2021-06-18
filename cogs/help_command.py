import discord
from discord.ext import commands
import json

print("Initializing help command")
with open("variables.json", "r") as var_able:
    variables = json.load(var_able)


class Help(commands.Cog):
    """
    This whole class focuses on the 'help' argument, it has my paypal as my footer init
    """
    def __init__(self, client):
        client.remove_command("help")

        @client.group(invoke_without_command=True, aliases=["help"])
        async def he_lp(ctx):
            em = discord.Embed(title="Help", description=f"Use `{variables['prefix']}"
                                                         f"help <command>` to get detailed view of that command",
                               colour=0xAAEEAA)
            em.add_field(name="Shit commands", value="ping, profile, tothedeveloper")
            em.add_field(name="Fun", value="pp, gayrate, simprate, ask, meme, snipe, emojify, ")
            em.add_field(name="NSFW", value="ass")
            em.add_field(name="Moderation", value="purge, kick, ban, unban, mute, unmute")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(f"Where you stuck step sista? :pinching_hand:<:trollface:849889411641507850>",
                            mention_author=False)
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command()
        async def ping(ctx):
            em = discord.Embed(title="**ping**", description="shows the ping between you and the server",
                               colour=0xAAEEAA)
            em.add_field(name="syntax", value=f"`{variables['prefix']}ping`")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command(aliases=["pfp"])
        async def profile(ctx):
            em = discord.Embed(title="**profile**", description="shows the info about the mention user if any",
                               colour=0xAAEEAA)
            em.add_field(name="syntax", value=f"`{variables['prefix']}profile [@user]`")
            em.add_field(name="aliases", value="`pfp`")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command()
        async def pp(ctx):
            em = discord.Embed(title="**pp**", description="shows the pp size, never lies", colour=0xFFAAFF)
            em.add_field(name="syntax", value=f"`{variables['prefix']}pp [@user]`")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command(aliases=["gay", "gr"])
        async def gayrate(ctx):
            em = discord.Embed(title="**gayrate**", description="shows how gay a user is, never lies", colour=0xFFCCAA)
            em.add_field(name="syntax", value=f"`{variables['prefix']}gayrate [@user]`")
            em.add_field(name="aliases", value="`gay, gr`")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command(aliases=["simp", "sr"])
        async def simprate(ctx):
            em = discord.Embed(title="**simprate**", description="show how much a person is", colour=0xAACCFF)
            em.add_field(name="syntax", value=f"`{variables['prefix']}simprate [@user]`")
            em.add_field(name="aliases", value="`simp, sr`")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command(aliases=["8ball"])
        async def ask(ctx):
            em = discord.Embed(title="**ask**", description="replies to your question, (probably)",
                               colour=0xAAEEAA)
            em.add_field(name="syntax", value=f"`{variables['prefix']}ask <question>`")
            em.add_field(name="aliases", value="`8ball`")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command()
        async def meme(ctx):
            em = discord.Embed(title="**meme**", description="shows a cursed meme", colour=0x00FFFF)
            em.add_field(name="syntax", value=f"`{variables['prefix']}meme`")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command()
        async def ass(ctx):
            em = discord.Embed(title="**ass**", description="If you know, you know", colour=0xFFFF00)
            em.add_field(name="syntax", value=f"{variables['prefix']}ass")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command(aliases=["tothedev", "tothedeveloper"])
        async def ttd(ctx):
            em = discord.Embed(title="**tothedeveloper**", description="sends the message to the developer",
                               colour=0xAAEEAA)
            em.add_field(name="syntax", value=f"`{variables['prefix']}tothedeveloper <message>`")
            em.add_field(name="aliases", value=f"`ttd, tothedev`")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command(aliases=["fuckoff"])
        async def ban(ctx):
            em = discord.Embed(title="**ban**", description="", colour=0x00FF44)
            em.add_field(name="syntax", value=f"`{variables['prefix']}ban [user] <reason>`")
            em.add_field(name="aliases", value="`fuckoff`")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command(aliases=["cumhere"])
        async def unban(ctx):
            em = discord.Embed(title="**unban**", description="unbans the given user", colour=0x00FF44)
            em.add_field(name="syntax", value=f"`{variables['prefix']}unban [user#0000]`")
            em.add_field(name="aliases", value="`cumhere`")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command(aliases=[])
        async def kick(ctx):
            em = discord.Embed(title="**kick**", description="kicks the member outta server", colour=0x00FF44)
            em.add_field(name="syntax", value=f"`{variables['prefix']}kick [@user] <reason>`")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command(aliases=["clear"])
        async def purge(ctx):
            em = discord.Embed(title="**clear**", description="deletes the number of message as given, max is 420",
                               colour=0x00FF44)
            em.add_field(name="syntax", value=f"`{variables['prefix']}(amount)`")
            em.add_field(name="aliases", value="`clear`")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command(aliases=["hitler, korea, stfu"])
        async def mute(ctx):
            em = discord.Embed(title="**mute**", description="mutes the fucking user",
                               colour=0xFFBBAA)
            em.add_field(name="syntax", value=f"`{variables['prefix']}mute [@user] (time) "
                                              "{unit} <reason>`")
            em.add_field(name="aliases", value="`hitler, korea, stfu, tempmute`")
            em.add_field(name="examples", value=f"{variables['prefix']}mute @bugs 1 w\n"
                                                f"{variables['prefix']}stfu @aayush 1 h chutiya")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command(aliases=["bolo"])
        async def unmute(ctx):
            em = discord.Embed(title="**unmute**", description="unmutes the unfucking member",
                               colour=0xFFBBAA)
            em.add_field(name="syntax", value=f"`{variables['prefix']}[@user]`")
            em.add_field(name="aliases", value="`bolo`")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)

        @he_lp.command()
        async def snipe(ctx):
            em = discord.Embed(title="**snipe**", description="snipes what the fucking user deleted",
                               colour=0x99DDDD)
            em.add_field(name="syntax", value=f"`{variables['prefix']}snipe`")
            em.add_field(name="aliases", value="`grandma`")
            em.set_footer(text="https://paypal.me/aumshreeshah")
            await ctx.reply(embed=em, mention_author=False)


def setup(client):
    client.add_cog(Help(client))
