# If you defined a custom Raise for custom Errors add them before everything else
# If that is related to prefix commands add it to the prefix commands section and if it is related to slash commands add it to the slash commands section after channel is defined

import discord
from discord import app_commands
from discord.ext import commands


class MyErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.tree.on_error = (
            self.on_app_command_error
        )  # This is necessary to handle errors in app commands

    # This is for prefix commands errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        channel = (
            ctx.guild.system_channel
        )  # Change it to the channel you want to send the unknown errors.
        # FlagError
        if isinstance(error, commands.BadFlagArgument):
            await ctx.reply(
                f"Bad flag argument\n**FlagName:** {error.flag_name}\n**Argument:** {error.argument}\n**Original:** {error.original}"
            )
        elif isinstance(error, commands.MissingFlagArgument):
            await ctx.reply(f"Missing flag argument\n**FlagName:** {error.flag_name}")
        elif isinstance(error, commands.TooManyFlags):
            await ctx.reply(
                f"Too many flags\n**Flags:** {error.flags}\n**Values:** {error.values}"
            )
        elif isinstance(error, commands.MissingRequiredFlag):
            await ctx.reply(f"Missing required flag\n**FlagName:** {error.flag_name}")
        # BadArgument
        elif isinstance(error, commands.ThreadNotFound):
            await ctx.reply(f"Thread not found\n**Argument:** {error.argument}")
        elif isinstance(error, commands.RangeError):
            await ctx.reply(
                f"Range error\n**Minimum:** {error.minimum}\n**Maximum:** {error.maximum}\n**Value:** {error.value}"
            )
        elif isinstance(error, commands.BadBoolArgument):
            await ctx.reply(f"Bad bool argument\n**Argument:** {error.argument}")
        elif isinstance(error, commands.PartialEmojiConversionFailure):
            await ctx.reply(
                f"Partial emoji conversion failure\n**Argument:** {error.argument}"
            )
        elif isinstance(error, commands.ScheduledEventNotFound):
            await ctx.reply(
                f"Scheduled event not found\n**Argument:** {error.argument}"
            )
        elif isinstance(error, commands.GuildStickerNotFound):
            await ctx.reply(f"Guild sticker not found\n**Argument:** {error.argument}")
        elif isinstance(error, commands.EmojiNotFound):
            await ctx.reply(f"Emoji not found\n**Argument:** {error.argument}")
        elif isinstance(error, commands.BadInviteArgument):
            await ctx.reply(f"Bad invite argument\n**Argument:** {error.argument}")
        elif isinstance(error, commands.RoleNotFound):
            await ctx.reply(f"Role not found\n**Argument:** {error.argument}")
        elif isinstance(error, commands.BadColourArgument):
            await ctx.reply(f"Bad colour argument\n**Argument:** {error.argument}")
        elif isinstance(error, commands.ChannelNotReadable):
            await ctx.reply(f"Channel not readable\n**Argument:** {error.argument}")
        elif isinstance(error, commands.ChannelNotFound):
            await ctx.reply(f"Channel not found\n**Argument:** {error.argument}")
        elif isinstance(error, commands.UserNotFound):
            await ctx.reply(f"User not found\n**Argument:** {error.argument}")
        elif isinstance(error, commands.GuildNotFound):
            await ctx.reply(f"Guild not found\n**Argument:** {error.argument}")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.reply(f"Member not found\n**Argument:** {error.argument}")
        elif isinstance(error, commands.MessageNotFound):
            await ctx.reply(f"Message not found\n**Argument:** {error.argument}")
        # ArgumentParsingError
        elif isinstance(error, commands.UnexpectedQuoteError):
            await ctx.typing()
        elif isinstance(error, commands.CommandNotFound):
            await ctx.reply(f"Command not found.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f"Missing required argument.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply(f"Missing permissions.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply(f"Bot missing permissions.")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(f"Command on cooldown.")
        elif isinstance(error, commands.NotOwner):
            await ctx.reply(f"This is an owner only command.")
        elif isinstance(error, commands.DisabledCommand):
            await ctx.reply(f"Disabled command.")
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.reply(f"No private message.")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.reply(f"Command invoke error.")
        elif isinstance(error, commands.CommandRegistrationError):
            await ctx.reply(f"Command registration error.")
        elif isinstance(error, commands.CommandError):
            await ctx.reply(f"Command error.\n```\n{error}\n```")
            raise error
        elif isinstance(error, commands.CheckFailure):
            await ctx.reply(f"Check failure.")
        elif isinstance(error, commands.UserInputError):
            await ctx.reply(f"User input error.")
        elif isinstance(error, commands.ConversionError):
            await ctx.reply(f"Conversion error.")
        elif isinstance(error, commands.BadArgument):
            await ctx.reply(f"Bad argument.")
        elif isinstance(error, commands.ArgumentParsingError):
            await ctx.reply(f"Argument parsing error.")
        elif isinstance(error, commands.TooManyArguments):
            await ctx.reply(f"Too many arguments.")
        elif isinstance(error, commands.ExpectedClosingQuoteError):
            await ctx.reply(f"Expected closing quote error.")
        elif isinstance(error, commands.InvalidEndOfQuotedStringError):
            await ctx.reply(f"Invalid end of quoted string error.")
        # Unknow error
        else:
            await channel.send(f"Unknown error:\n```txt\n{error}\n```")

    # This is for slash commands errors
    async def on_app_command_error(self, interaction: discord.Interaction, error):
        channel = interaction.guild.system_channel
        if isinstance(error, app_commands.errors.CommandInvokeError):
            await channel.send(
                f"Command invoke error.\n```py\n{app_commands.errors.CommandInvokeError().command} raised \n{app_commands.errors.CommandInvokeError().original}```"
            )
        elif isinstance(error, app_commands.errors.TransformerError):
            await interaction.response.send_message(f"Transformer error.")
        elif isinstance(error, app_commands.errors.TranslationError):
            await interaction.response.send_message(f"Translation error.")
        elif isinstance(error, app_commands.errors.NoPrivateMessage):
            await interaction.response.send_message(f"No private message.")
        elif isinstance(error, app_commands.errors.MissingRole):
            await interaction.response.send_message(error)
        elif isinstance(error, app_commands.errors.MissingAnyRole):
            await interaction.response.send_message(
                f"Missing any role.{app_commands.errors.MissingAnyRole().missing_roles}"
            )
        elif isinstance(error, app_commands.errors.MissingPermissions):
            await interaction.response.send_message(
                f"Missing permissions. {app_commands.errors.MissingPermissions().missing_permissions}"
            )
        elif isinstance(error, app_commands.errors.BotMissingPermissions):
            await interaction.response.send_message(
                f"Bot missing permissions. {app_commands.errors.BotMissingPermissions().missing_permissions}"
            )
        elif isinstance(error, app_commands.errors.CommandOnCooldown):
            await interaction.response.send_message(
                f"Command on {app_commands.errors.CommandOnCooldown().cooldown}. {app_commands.errors.CommandOnCooldown().retry_after}"
            )
        elif isinstance(error, app_commands.errors.CheckFailure):
            await interaction.response.send_message(f"Check failure.")
        elif isinstance(error, app_commands.errors.CommandLimitReached):
            await interaction.response.send_message(
                f"Command limit reached.\n**Guild_ID:** {app_commands.errors.CommandLimitReached().guild_id}\n**Limit:** {app_commands.errors.CommandLimitReached().limit}\m**TYPE:**{app_commands.errors.CommandLimitReached().type}"
            )
        elif isinstance(error, app_commands.errors.CommandAlreadyRegistered):
            await interaction.response.send_message(
                f"Command already registered.\n**Name:** {app_commands.errors.CommandAlreadyRegistered().name}\n**Guild_id:** {app_commands.errors.CommandAlreadyRegistered().guild_id}"
            )
        elif isinstance(error, app_commands.errors.CommandSignatureMismatch):
            await interaction.response.send_message(
                f"Command signature mismatch.{app_commands.errors.CommandSignatureMismatch().signature}"
            )
        elif isinstance(error, app_commands.errors.CommandNotFound):
            await interaction.response.send_message(f"Command not found.")
        elif isinstance(error, app_commands.errors.MissingApplicationID):
            await interaction.response.send_message(f"Missing application ID.")
        elif isinstance(error, app_commands.errors.CommandSyncFailure):
            await interaction.response.send_message(f"Command sync failure.")
        # Unknow error
        else:
            await channel.send(f"Unknown error:\n```txt\n{error}\n```")


async def setup(bot):
    await bot.add_cog(MyErrorHandler(bot))
