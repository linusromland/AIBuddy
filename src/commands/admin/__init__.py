""" Index file for admin commands. """
import os
from sqlite3 import Connection
from discord import Object, app_commands
from commands.admin.add_admin_command import setup as add_admin_setup
from commands.admin.list_admins_command import setup as list_admins_setup
from commands.admin.remove_admin_command import setup as remove_admin_setup


def register_commands(tree: app_commands.CommandTree, conn: Connection, guild_id: str | None) -> None:
    """ Register all admin commands. """
    add_admin_setup(tree, conn, guild_id)
    list_admins_setup(tree, conn, guild_id)
    remove_admin_setup(tree, conn, guild_id)
