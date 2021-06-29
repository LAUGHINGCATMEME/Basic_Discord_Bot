import asyncio
import discord
from discord.ext import commands
import json

print("Initializing Permissions commands")
with open("variables.json", "r") as var_able:
    variables = json.load(var_able)
snipe_message_content = []
snipe_message_author = []
snipe_guild_id = []
prefix = variables["prefix"]
num = len(prefix)


class Moderation(commands.Cog):
    """
    This whole class has Moderation events,
    please check the commands coz there are some problems which im too tired to fix, one of which is
    a mod can ban other mod by ban command
    """
    def __init__(self, client):
        @client.event
        async def on_message_delete(message):
            global snipe_message_content
            global snipe_message_author
            global snipe_guild_id
            snipe_message_content.append(message.content)
            snipe_message_author.append(message.author.name)
            snipe_guild_id.append(message.guild.id)
        self.client = client

    # @commands.Cog.listener() for event
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """
        kicks the member outta the server
        :param ctx: Message
        :param member: Member which user wants to kick
        :param reason: Reason for the kick
        :return:
        """
        if reason is None:
            reason = "nothing"
        km = discord.Embed(title="Kicked", description=f"{member} has been kicked for {reason}",
                           color=0x000000)
        await member.kick(reason=reason)
        km.set_footer(text=f"by {ctx.author.name}")
        await ctx.message.channel.send(embed=km)

    @kick.error
    async def kick_error(self, ctx, error):
        """
        In the case the kick commands rises a given error
        :param ctx: Message
        :param error: Error raised
        """
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f"**User missing Try:**\n`{prefix}kick <@user> [reason]`", mention_author=False)
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.reply(f"You don't have permission to kick members.", mention_author=False)

    @commands.command(aliases=["clear"])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=0):
        """
        Purges the given amount of messages in the channel, the max limit is 420 also there is no cooldown in it so the
        person who has manage messages permissions can purge the whole channel be spamming the command
        :param ctx: Message
        :param amount: the amount of message user wants to delete
        :return:
        """
        if amount > 420 or amount < 0:
            await ctx.reply(f"**Clear amount must be between 1 - 420**", mention_author=False)
        else:
            amount += 1
            await ctx.channel.purge(limit=amount)
            await ctx.channel.send(f"{amount - 1} messages has been purged")

    @purge.error
    async def clear_error(self, ctx, error):
        """
        In the case the clear command rises a given error
        :param ctx: Message
        :param error: Error raised
        """
        if isinstance(error, commands.errors.MissingPermissions):
            cmd = ((ctx.message.content[num::]).split(" "))[0]
            await ctx.reply(f"You don't have permission to use {cmd}.", mention_author=False)

    @commands.command(aliases=["fuck" + "off"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """
        Bans the user outta the guild, im too lazy to make a tempban command
        :param ctx: Message
        :param member: Member which user wants to ban
        :param reason: Reason for the ban
        :return:
        """
        if reason is None:
            reason = "nothing"
        bm = discord.Embed(title="Banned", description=f"{member} has been banned for {reason}", color=0x000000)
        await member.ban(reason=reason)
        bm.set_footer(text=f"by {ctx.author.name}")
        await ctx.message.channel.send(embed=bm)

    @ban.error
    async def ban_error(self, ctx, error):
        """
        In the case the ban command rises a given error
        :param ctx: Message
        :param error: Error raised
        """
        if isinstance(error, commands.MissingRequiredArgument):
            cmd = ((ctx.message.content[num::]).split(" "))[0]
            await ctx.reply(f"**User missing Try:**\n`{prefix}{cmd} <@user> [reason]`", mention_author=False)
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.reply(f"You don't have permission to ban members.", mention_author=False)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        """
        Unbans the member
        :param ctx: Message
        :param member: Member which user wants to unban
        :return:
        """
        ban_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for entries in ban_users:
            user = entries.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                unb = discord.Embed(title="Unbanned", description=f"{member} has been Unbanned", color=0XFFFFFF)
                unb.set_footer(text=f"by {ctx.author.name}")
                await ctx.send(embed=unb)
                return

    @unban.error
    async def unban_error(self, ctx, error):
        """
        In the case the unban command rises a given error
        :param ctx: Message
        :param error: Error raised
        """
        if isinstance(error, commands.MissingRequiredArgument):
            cmd = ((ctx.message.content[num::]).split(" "))[0]
            await ctx.reply(f"**User missing Try:**\n`{prefix}{cmd} <user#0000>`", mention_author=False)
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.reply(f"You don't have permission to unban members.", mention_author=False)

    @commands.command(aliases=["hitler", "korea", "stfu"])
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, sting=None):
        """
        This is the command which has a lot of problems which I still need to fix, like incase a mod uses this command
        on another mod, it'll give him a mute role but as the user is a mod he'll still be able to talk
        :param ctx: Message
        :param member: Member which user wants to mute
        :param sting: Reason for the mute
        :return:
        """
        try:
            if sting is None:
                # The default mute time
                all_variables = ["5", "h"]
            else:
                all_variables = sting.split(" ")
            all_variables[0] = int(all_variables[0])
            if len(all_variables) == 1:
                # When the unit of the time is not given
                await ctx.reply(f"Arguments not given properly,\nTry typing `{prefix}help mute`", mention_author=False)
                return
            elif len(all_variables) == 2:
                all_variables.append("nothing")
            if all_variables[0] > 1:
                # To correct the grammer lol, yes
                s_p = "s"
            else:
                s_p = ""
            if all_variables[1].upper() == "S" or all_variables[1].upper() == "SEC" or \
                    all_variables[1].upper() == "SECOND":
                mute_time, s_tax = all_variables[0], "second"
            elif all_variables[1].upper() == "M" or all_variables[1].upper() == "MIN" or \
                    all_variables[1].upper() == "MINTUE":
                mute_time, s_tax = all_variables[0] * 60, "minute"
            elif all_variables[1].upper() == "H" or all_variables[1].upper() == "HOUR":
                mute_time, s_tax = all_variables[0] * 3600, "hour"
            elif all_variables[1].upper() == "D" or all_variables[1].upper() == "DAY":
                mute_time, s_tax = all_variables[0] * 86400, "day"
            elif all_variables[1].upper() == "W" or all_variables[1].upper() == "WEEK":
                mute_time, s_tax = all_variables[0] * 604800, "week"
            else:
                await ctx.reply(f"Arguments not given properly,\nTry typing `{prefix}help mute`", mention_author=False)
                return
            # To many extra variables from here
            reason = ""
            reason_1 = all_variables[2::]
            for i in reason_1:
                reason += f"{i} "
        except ValueError:
            await ctx.reply(f"Arguments not given properly,\nTry typing `{prefix}help mute`", mention_author=False)
            return
        formate = str(all_variables[0]) + str(s_tax) + str(s_p)
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not role:
            role = await ctx.guild.create_role("Muted", permissions=discord.Permissions(send_messages=False))
        bm = discord.Embed(title="Muted", description=f"{member.mention} has been muted for {reason}", color=0x000000)
        bm.set_footer(text=f"by {ctx.author.name}, for {formate}")
        await member.add_roles(role)
        await ctx.message.channel.send(embed=bm)
        await asyncio.sleep(mute_time)
        await member.remove_roles(role)
        em = discord.Embed(title="Unmuted", description=f"{member.mention} has benn unmuted", colour=0xFFFFFF)
        em.set_footer(text=f"{formate} has passed")
        await ctx.message.channel.send(embed=em)

    @mute.error
    async def mute_error(self, ctx, error):
        """
        In the case the mute command rises a given error
        :param ctx: Message
        :param error: Error raised
        """
        if isinstance(error, commands.MissingRequiredArgument):
            cmd = ((ctx.message.content[num::]).split(" "))[0]
            await ctx.reply(f"**User missing Try:**\n`{prefix}{cmd} [@user]`", mention_author=False)
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.reply(f"You don't have permission to mute members.", mention_author=False)

    @commands.command(aliases=["bolo"])
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not role:
            role = await ctx.guild.create_role("Muted", permissions=discord.Permissions(send_messages=False))
        await member.remove_roles(role)
        bm = discord.Embed(title="Unuted", description=f"{member.mention} has been unmuted", color=0XFFFFFF)
        bm.set_footer(text=f"by {ctx.author.name}")
        await ctx.message.channel.send(embed=bm)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            cmd = ((ctx.message.content[num::]).split(" "))[0]
            await ctx.reply(f"**User missing Try:**\n`{prefix} {cmd}[@user]`", mention_author=False)
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.reply(f"You don't have permission to unmute members.", mention_author=False)

    @commands.command(aliases=["grandma"])
    async def snipe(self, ctx):
        """
        LOL this command snipe the last message from every guild, ill improve this later(prpbably)
        :param ctx: Message
        :return:
        """
        global snipe_message_content
        global snipe_message_author
        msg = snipe_message_content[::-1]
        aut = snipe_message_author[::-1]
        em = discord.Embed(title=f"", description=msg[0], colour=0x99DDDD)
        em.set_footer(text=f"deleted by {aut[0]}")
        await ctx.reply(embed=em, mention_author=False)

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member: discord.Member, *, nickname):
        """
        Changes the member nickname
        :param ctx: Message
        :param member: The member which name wants to be changed
        :param nickname: The nick
        :return:
        """
        await member.edit(nick=nickname)
        await ctx.reply(f"Changed {member.display_name}'s nickname to {nickname}'", mention_author=False)

    @commands.command(aliases=["deleteinv", "di"])
    @commands.has_permissions(manage_channels=True)
    async def del_invite(self, ctx, invite: discord.Invite):
        """
        I still need to and ~~some~~ MANY moderation commands but again, IM TOO LAZY
        :param ctx: Message
        :param invite: The invite which user wants to delete
        :return:
        """
        inv = await discord.Client.fetch_invite(self.client, invite)
        await discord.Client.delete_invite(self.client, inv)
        await ctx.reply("Invite deleted", mention_author=False)


def setup(client):
    client.add_cog(Moderation(client))
