""" Set general information command """

from sqlite3 import Connection
from discord import Interaction, Object, app_commands
from database.queries.general_info import get_information, set_information
from utils.check_permission import check_permission

conn: Connection


def setup(tree: app_commands.CommandTree, db_conn: Connection, guild_id: str | None) -> None:
    """ Setup the set general information command. """
    # Update the global connection variable
    global conn
    conn = db_conn

    @tree.command(
        name="set_general_information",
        description="Set the general information of the virtual member.",
        guild=Object(guild_id) if guild_id else None,
    )
    @app_commands.describe(key="The key of the information. (name, birthday, city or country)")
    @app_commands.describe(value="The value of the information.")
    async def _(interaction: Interaction, key: str, value: str):
        """ Trigger the set general information command. """
        await set_general_information(interaction, key, value)


async def set_general_information(interaction, key: str, value: str):
    """ Set the general information of the virtual member. """

    user_access = check_permission(conn, str(interaction.user.id), False)

    if not user_access:
        await interaction.response.send_message(
            "You do not have permission to use this command.", ephemeral=True)
        return

    if (key not in ["name", "birthday", "city", "country"]):
        await interaction.response.send_message(
            "Invalid key. Valid keys are: name, birthday, city or country", ephemeral=True)
        return

    set_information(conn, key, value)

    information = get_information(conn)

    if not information:
        await interaction.response.send_message(
            "No information found.", ephemeral=True)
        return

    await interaction.response.send_message(
        f"Updated `{key}` to `{value}`", ephemeral=True)
