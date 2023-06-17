""" Add miscellaneous information command """

from sqlite3 import Connection
from discord import Interaction, Object, app_commands
from database.queries.misc_info import add_misc_info
from utils.check_permission import check_permission

conn: Connection


def setup(tree: app_commands.CommandTree, db_conn: Connection, guild_id: str | None) -> None:
    """ Setup the add miscellaneous information command """
    # Update the global connection variable
    global conn
    conn = db_conn

    @tree.command(
        name="add_misc_information",
        description="Add miscellaneous information that does not fit into the general information.",
        guild=Object(guild_id) if guild_id else None,
    )
    @app_commands.describe(information="The information you want to add. (Separate multiple information with a semicolon(;))")
    async def _(interaction: Interaction, information: str):
        """ Trigger the add misc information command. """
        await add_misc_information(interaction, information)


async def add_misc_information(interaction, information: str):
    """ Add miscellaneous information to the virtual member. """

    user_access = check_permission(conn, str(interaction.user.id), False)

    if not user_access:
        await interaction.response.send_message(
            "You do not have permission to use this command.", ephemeral=True)
        return

    split_information = information.split(";")

    for info in split_information:
        add_misc_info(conn, info)

    await interaction.response.send_message(
        f"Added {len(split_information)} information(s).", ephemeral=True)
