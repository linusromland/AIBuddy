""" Message Answer Handler. """
import asyncio
from discord import Client, Message


async def answer_message(message: Message, client: Client):
    """ Handle message answering. """
    # Enable typing indicator
    async with message.channel.typing():
        # Replace with OpenAI API call
        await asyncio.sleep(15)

    # Send the answer
    await message.reply("Hello, I am a bot!")
