""" Index file for miscellaneous info commands. """
import os
from sqlite3 import Connection
from discord import app_commands
from commands.misc_information.add_misc_information_command import setup as add_misc_information_setup
from commands.misc_information.list_misc_information_command import setup as list_misc_information_setup
from commands.misc_information.remove_misc_information_command import setup as remove_misc_information_setup


def register_commands(tree: app_commands.CommandTree, conn: Connection, guild_id: str | None) -> None:
    """ Register all miscellaneous info commands. """
    add_misc_information_setup(tree, conn, guild_id)
    list_misc_information_setup(tree, conn, guild_id)
    remove_misc_information_setup(tree, conn, guild_id)
