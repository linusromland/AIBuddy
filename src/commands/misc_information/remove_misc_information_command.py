""" Remove miscellaneous information command """

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
        description="Remove a miscellaneous information entry. (Use list_misc_information to get the id)",
        guild=Object(guild_id) if guild_id else None,
    )
    @app_commands.describe(misc_info_ids="The id of the miscellaneous information you want to remove. (Separate multiple ids with a semicolon(;))")
    async def _(interaction: Interaction, misc_info_ids: str):
        """ Trigger the remove miscellaneous information command. """
        await remove_misc_information(interaction, misc_info_ids)


async def remove_misc_information(interaction, misc_info_ids: str):
    """ Remove miscellaneous information to the virtual member. """

    user_access = check_permission(conn, str(interaction.user.id), False)

    if not user_access:
        await interaction.response.send_message(
            "You do not have permission to use this command.", ephemeral=True)
        return

    split_misc_info_ids = misc_info_ids.split(";")

    for misc_info_id in split_misc_info_ids:
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
        f"Removed {len(split_misc_info_ids)} miscellaneous information(s).", ephemeral=True)
