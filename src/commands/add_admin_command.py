""" Add Admin command """

from sqlite3 import Connection
from discord import Enum, Interaction, Object, User, app_commands
from utils.check_permission import check_permission
from database.queries.admin import get_all_admins, add_admin as add_admin_db, remove_admin as remove_admin_db

conn: Connection


class AdminPermissons(Enum):
    """ The permissons for an admin. """
    FULL_ACCESS = 2
    PARTIAL_ACCESS = 1


def setup(tree: app_commands.CommandTree, db_conn: Connection, guild_id: str | None) -> None:
    """ Setup the add admin command. """
    # Update the global connection variable
    global conn
    conn = db_conn

    @tree.command(
        name="add_admin",
        description="Add an admin. (FULL=Can edit backstory, PARTIAL=Can make bot forget previous messages)",
        guild=Object(guild_id) if guild_id else None,
    )
    @app_commands.describe(user="The user to add as an admin.")
    @app_commands.describe(permisson="The permisson level of the user.")
    async def _(interaction: Interaction, user: User, permisson: AdminPermissons):
        """ Trigger the permisson command. """
        await add_admin(interaction, user, permisson)


async def add_admin(interaction, user: User, permisson: AdminPermissons):
    """ Add an admin to the bot. """
    admins = get_all_admins(conn)

    user_access = check_permission(conn, str(interaction.user.id), False)

    if not user_access:
        await interaction.response.send_message(
            "You do not have permission to use this command.", ephemeral=True)
        return

    admin = next(
        (admin for admin in admins if admin["discord_id"] == str(user.id)), None)

    if admin and admin['permission_level'] == permisson.value:
        await interaction.response.send_message(
            f"`{user.name}` is already an admin with `{permisson.name}` permissions.", ephemeral=True)
        return
    elif admin:
        remove_admin_db(conn, str(user.id))
        add_admin_db(conn, str(user.id), permisson.value)
        await interaction.response.send_message(f"Updated admin `{user.name}` to `{permisson.name}`", ephemeral=True)
        return

    add_admin_db(conn, str(user.id), permisson.value)
    await interaction.response.send_message(
        f"Added admin `{user.name}` with `{permisson.name}`", ephemeral=True)
