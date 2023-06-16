""" Ping command """

from discord import Interaction, Object, app_commands


def setup(tree: app_commands.CommandTree, guild_id: str | None) -> None:
    """ Setup the ping command. """

    @tree.command(
        name="ping",
        description="Ping the bot",
        guild=Object(guild_id) if guild_id else None,
    )
    async def _(interaction: Interaction):
        """ Trigger the ping command. """
        await ping(interaction)


async def ping(interaction):
    """ Ping the bot. """
    await interaction.response.send_message("Pong!")
