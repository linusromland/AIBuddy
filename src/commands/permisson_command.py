""" Permisson command """

from sqlite3 import Connection
from discord import Interaction, Object, User, app_commands
from utils.check_permission import check_permission
from database.queries.admin import get_all_admins

conn: Connection


def setup(tree: app_commands.CommandTree, db_conn: Connection, guild_id: str | None) -> None:
    """ Setup the permisson command. """
    # Update the global connection variable
    global conn
    conn = db_conn

    @tree.command(
        name="check_permisson",
        description="Get the permission level of a user.",
        guild=Object(guild_id) if guild_id else None,
    )
    @app_commands.describe(user="The user to get the permission level of.")
    async def _(interaction: Interaction, user: User):
        """ Trigger the permisson command. """
        await permisson(interaction, user)


async def permisson(interaction, user: User):
    """ Retrieve the permission level of a user. """
    admins = get_all_admins(conn)

    user_access = check_permission(conn, str(interaction.user.id), False)

    if not user_access and interaction.user.id != interaction.guild.owner_id:
        await interaction.response.send_message(
            "You do not have permission to use this command.", ephemeral=True)
        return

    admin = next(
        (admin for admin in admins if admin["discord_id"] == str(user.id)), None)

    if admin:
        await interaction.response.send_message(
            f"`{user.name}` has {'full' if admin['permission_level'] == 2 else 'partial'} permissions.", ephemeral=True)
        return

    await interaction.response.send_message(
        f"`{user.name}` has no permissions.", ephemeral=True)
