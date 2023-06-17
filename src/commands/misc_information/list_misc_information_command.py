""" List miscellaneous information command """

from sqlite3 import Connection
from discord import Embed, Interaction, Object, app_commands
from database.queries.misc_info import get_all_misc_info
from utils.check_permission import check_permission

conn: Connection


def setup(tree: app_commands.CommandTree, db_conn: Connection, guild_id: str | None) -> None:
    """ Setup the list miscellaneous information command """
    # Update the global connection variable
    global conn
    conn = db_conn

    @tree.command(
        name="list_misc_information",
        description="List all miscellaneous information for the virtual member.",
        guild=Object(guild_id) if guild_id else None,
    )
    async def _(interaction: Interaction):
        """ Trigger the list misc information command. """
        await list_misc_information(interaction)


async def list_misc_information(interaction):
    """ List misc information to the virtual member. """

    user_access = check_permission(conn, str(interaction.user.id), False)

    if not user_access:
        await interaction.response.send_message(
            "You do not have permission to use this command.", ephemeral=True)
        return

    misc_info = get_all_misc_info(conn)

    if not misc_info:
        await interaction.response.send_message(
            "No miscellaneous information found.", ephemeral=True)
        return

    embed = Embed(title="miscellaneous Information", color=0x00ff00)
    for info in misc_info:
        embed.add_field(name=info["id"],
                        value=info["info"], inline=False)

    await interaction.response.send_message(embed=embed, ephemeral=True)
