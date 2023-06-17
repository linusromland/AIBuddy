""" Add Admin command """

from sqlite3 import Connection
from discord import Interaction, Object, User, app_commands
from utils.check_permission import check_permission
from database.queries.admin import get_all_admins, remove_admin as remove_admin_db

conn: Connection


def setup(tree: app_commands.CommandTree, db_conn: Connection, guild_id: str | None) -> None:
    """ Setup the remove admin command. """
    # Update the global connection variable
    global conn
    conn = db_conn

    @tree.command(
        name="remove_admin",
        description="Remove an admin.",
        guild=Object(guild_id) if guild_id else None,
    )
    @app_commands.describe(user="The user to add as an admin.")
    async def _(interaction: Interaction, user: User):
        """ Trigger the remove admin command. """
        await remove_admin(interaction, user)


async def remove_admin(interaction, user: User):
    """ Remove an admin to the bot. """
    admins = get_all_admins(conn)

    user_access = check_permission(conn, str(interaction.user.id), True)

    if not user_access:
        await interaction.response.send_message(
            "You do not have permission to use this command.", ephemeral=True)
        return

    admin = next(
        (admin for admin in admins if admin["discord_id"] == str(user.id)), None)

    if not admin:
        await interaction.response.send_message(
            f"`{user.name}` is not an admin.", ephemeral=True)
        return

    if admin and admin['permission_level'] == 3:
        await interaction.response.send_message(
            f"`{user.name}` is the owner of the bot and cannot be removed.", ephemeral=True)
        return

    remove_admin_db(conn, str(user.id))
    await interaction.response.send_message(f"Removed admin `{user.name}`", ephemeral=True)
