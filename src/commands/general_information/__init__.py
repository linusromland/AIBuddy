""" Index file for general info commands. """
import os
from sqlite3 import Connection
from discord import app_commands
from commands.general_information.get_general_information_command import setup as get_general_information_setup
from commands.general_information.set_general_information_command import setup as set_general_information_setup


def register_commands(tree: app_commands.CommandTree, conn: Connection, guild_id: str | None) -> None:
    """ Register all general info commands. """
    get_general_information_setup(tree, conn, guild_id)
    set_general_information_setup(tree, conn, guild_id)
