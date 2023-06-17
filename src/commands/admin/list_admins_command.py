""" List Admins command """

from sqlite3 import Connection
from discord import Embed, Interaction, Object, app_commands
from utils.check_permission import check_permission
from utils.format_permisson import format_permisson
from database.queries.admin import get_all_admins

conn: Connection


def setup(tree: app_commands.CommandTree, db_conn: Connection, guild_id: str | None) -> None:
    """ Setup the List Admins command. """
    # Update the global connection variable
    global conn
    conn = db_conn

    @tree.command(
        name="list_admins",
        description="Get the list of admins.",
        guild=Object(guild_id) if guild_id else None,
    )
    async def _(interaction: Interaction):
        """ Trigger the permisson command. """
        await list_admins(interaction)


async def list_admins(interaction):
    """ Retrieve the permission level of all users. """

    user_access = check_permission(conn, str(interaction.user.id), False)

    if not user_access:
        await interaction.response.send_message(
            "You do not have permission to use this command.", ephemeral=True)
        return

    admins = get_all_admins(conn)

    embed = Embed(title="Admins", color=0x00ff00)

    for admin in admins:
        user = interaction.guild.get_member(int(admin["discord_id"]))

        embed.add_field(
            name=user.name if user else admin["discord_id"], value=format_permisson(admin["permission_level"]), inline=False)

    await interaction.response.send_message(embed=embed, ephemeral=True)
