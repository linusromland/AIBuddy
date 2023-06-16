import os
from discord import Interaction, app_commands
from .ping_command import setup as ping_setup

GUILD_ID = os.getenv("GUILD_ID")


def register_commands(tree: app_commands.CommandTree) -> None:
    ping_setup(tree, GUILD_ID)
