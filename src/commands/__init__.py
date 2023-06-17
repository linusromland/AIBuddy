""" Index file for commands. """
import os
from sqlite3 import Connection
from discord import Object, app_commands
from commands.permisson_command import setup as permisson_setup

GUILD_ID = os.getenv("GUILD_ID")


async def register_commands(tree: app_commands.CommandTree, conn: Connection) -> None:
    """ Register all commands. """
    permisson_setup(tree, conn, GUILD_ID)

    # Sync the commands with the Discord API
    await tree.sync(guild=Object(GUILD_ID if GUILD_ID else ""))
