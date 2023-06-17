""" Add remove. information command """

from sqlite3 import Connection
from discord import Interaction, Object, app_commands
from database.queries.misc_info import misc_info_exists, remove_misc_info
from utils.check_permission import check_permission

conn: Connection


def setup(tree: app_commands.CommandTree, db_conn: Connection, guild_id: str | None) -> None:
    """ Setup the remove miscellaneous information command """
    # Update the global connection variable
    global conn
    conn = db_conn

    @tree.command(
        name="remove_misc_information",
        description="Remove a miscellaneous information entry.",
        guild=Object(guild_id) if guild_id else None,
    )
    @app_commands.describe(misc_info_id="The id of the miscellaneous information you want to remove. (Use list_misc_information to get the id)")
    async def _(interaction: Interaction, misc_info_id: str):
        """ Trigger the remove misc information command. """
        await remove_misc_information(interaction, misc_info_id)


async def remove_misc_information(interaction, misc_info_id: str | int):
    """ Remove misc information to the virtual member. """

    user_access = check_permission(conn, str(interaction.user.id), False)

    if not user_access:
        await interaction.response.send_message(
            "You do not have permission to use this command.", ephemeral=True)
        return

    try:
        misc_info_id = int(misc_info_id)
    except ValueError:
        await interaction.response.send_message(
            "The miscellaneous information id must be a number.", ephemeral=True)
        return

    if not misc_info_exists(conn, int(misc_info_id)):
        await interaction.response.send_message(
            "The miscellaneous information id does not exist.", ephemeral=True)
        return

    remove_misc_info(conn, int(misc_info_id))

    await interaction.response.send_message(
        f"Removed miscellaneous information with id: {misc_info_id}", ephemeral=True)
