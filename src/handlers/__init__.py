""" Index file for handlers. """
from discord import Client
from sqlite3 import Connection
from handlers.message_handler import setup as setup_message_handler


async def register_handlers(client: Client, conn: Connection) -> None:
    """ Register all handlers. """
    setup_message_handler(client, conn)
