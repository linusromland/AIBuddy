""" Index file for handlers. """
from discord import Client
from handlers.message_handler import setup as setup_message_handler


async def register_handlers(client: Client) -> None:
    """ Register all handlers. """
    setup_message_handler(client)
