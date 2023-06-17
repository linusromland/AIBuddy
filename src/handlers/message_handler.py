""" Message Handler. """
from discord import Client, Message


def setup(client: Client) -> None:
    """ Setup the message handler. """
    @client.event
    async def on_message(message: Message) -> None:
        """ Handle messages. """
        await handle_on_message(message)


async def handle_on_message(message: Message):
    """ Retrieve the permission level of all users. """
    print(message.content)
