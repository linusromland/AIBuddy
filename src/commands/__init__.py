""" Index file for commands. """
import os
from sqlite3 import Connection
from discord import Object, app_commands
from commands.add_admin_command import setup as add_admin_setup
from commands.permisson_command import setup as permisson_setup


GUILD_ID = os.getenv("GUILD_ID")


async def register_commands(tree: app_commands.CommandTree, conn: Connection) -> None:
    """ Register all commands. """
    add_admin_setup(tree, conn, GUILD_ID)
    permisson_setup(tree, conn, GUILD_ID)

    # Sync the commands with the Discord API
    await tree.sync(guild=Object(GUILD_ID if GUILD_ID else ""))
