""" Message Answer Handler. """
from sqlite3 import Connection
from discord import Client, Message
from database.queries.general_info import get_information
from database.queries.misc_info import get_all_misc_info
from utils.openai_api import generate_response


async def answer_message(message: Message, client: Client, conn: Connection):
    """ Handle message answering. """
    # Enable typing indicator
    await message.channel.typing()

    # Get the general information
    general_info = get_information(conn)

    # Get all miscellaneous information
    misc_info = get_all_misc_info(conn)

    if not general_info:
        await message.reply("No information found.")
        return

    system_prompt = f"You are a member of a discord server. You will response to the messages of the other members. You will pretend to be a human. Do not say or reveal you are a AI or a bot. You are a human. General Information about you: Name: {general_info['name']}. Birthday: {general_info['birthday']}. City: {general_info['city']}. Country: {general_info['country']}."

    if len(misc_info) > 0:
        system_prompt += " Additional information about you:"

    for info in misc_info:
        system_prompt += f" {info['info']}."

    system_prompt += "Anything that you do not know you make up. Do not repeat yourself. You will now start to answer the messages of the other members."

    prompt = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    # TODO: FIX SO THE MESSAGES ARE IN THE RIGHT ORDER
    async for previous_message in message.channel.history():
        prompt.append({
            "role": "assistant" if previous_message.author == client.user else "user",
            "content": previous_message.content
        })

    print(prompt)

    # Make call to OpenAI here
    response = generate_response(prompt)

    # Send the answer
    await message.reply(response)
