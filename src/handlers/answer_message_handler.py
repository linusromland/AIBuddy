""" Message Answer Handler. """
from sqlite3 import Connection
from discord import Message
from database.queries.general_info import get_information
from database.queries.misc_info import get_all_misc_info
from utils.openai_api import generate_text


async def answer_message(message: Message, conn: Connection):
    """ Handle message answering. """
    # Enable typing indicator
    await message.channel.typing()

    # Get the general information
    general_info = get_information(conn)

    # Get all miscellaneous information
    misc_info = get_all_misc_info(conn)

    previous_messages = message.channel.history(limit=10)

    print(general_info)
    print(misc_info)
    print(previous_messages)

    # Make call to OpenAI here
    response = generate_text(
        "Create a response to the message:" + message.content, 100)

    # Send the answer
    await message.reply(response)
