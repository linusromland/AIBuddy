""" Get general information command """

from sqlite3 import Connection
from discord import Embed, Interaction, Object, app_commands
from database.queries.general_info import get_information
from utils.check_permission import check_permission

conn: Connection


def setup(tree: app_commands.CommandTree, db_conn: Connection, guild_id: str | None) -> None:
    """ Setup the get general information command. """
    # Update the global connection variable
    global conn
    conn = db_conn

    @tree.command(
        name="get_general_information",
        description="Get the general information of the virtual member.",
        guild=Object(guild_id) if guild_id else None,
    )
    async def _(interaction: Interaction):
        """ Trigger the permisson command. """
        await get_general_information(interaction)


async def get_general_information(interaction):
    """ Retrieve the permission level of a user. """

    user_access = check_permission(conn, str(interaction.user.id), False)

    if not user_access:
        await interaction.response.send_message(
            "You do not have permission to use this command.", ephemeral=True)
        return

    information = get_information(conn)

    if not information:
        await interaction.response.send_message(
            "No information found.", ephemeral=True)
        return

    embed = Embed(title="General Information", color=0x00ff00)
    embed.add_field(name="Name", value=information["name"], inline=False)
    embed.add_field(name="Birthday",
                    value=information["birthday"], inline=False)
    embed.add_field(name="City", value=information["city"], inline=False)
    embed.add_field(name="Country", value=information["country"], inline=False)

    await interaction.response.send_message(embed=embed, ephemeral=True)
