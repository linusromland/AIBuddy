""" Message Handler. """
from random import randint
from discord import Client, Message
from handlers.answer_message_handler import answer_message


def setup(client: Client) -> None:
    """ Setup the message handler. """
    @client.event
    async def on_message(message: Message) -> None:
        """ Handle messages. """
        await handle_on_message(message, client)


async def handle_on_message(message: Message, client: Client):
    """ Handle messages. """
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    print(f"User: {message.author.name}#{message.author.discriminator} ({message.author.id}) said: {message.content}")

    # Answer if the bot is mentioned
    if client.user in message.mentions:
        return await answer_message(message, client)

    # Answer random messages with a 1/15 chance
    if randint(1, 15) == 1:
        return await answer_message(message, client)
