""" Index file for commands. """
import os
from sqlite3 import Connection
from discord import Object, app_commands
from commands.admin import register_commands as register_admin_commands
from commands.general_information import register_commands as register_general_information_commands
from commands.misc_information import register_commands as register_misc_information_commands
from commands.permisson_command import setup as permisson_setup

GUILD_ID = os.getenv("GUILD_ID")


async def register_commands(tree: app_commands.CommandTree, conn: Connection) -> None:
    """ Register all commands. """
    register_admin_commands(tree, conn, GUILD_ID)
    register_general_information_commands(tree, conn, GUILD_ID)
    register_misc_information_commands(tree, conn, GUILD_ID)
    permisson_setup(tree, conn, GUILD_ID)

    # Sync the commands with the Discord API
    await tree.sync(guild=Object(GUILD_ID) if GUILD_ID else None)
