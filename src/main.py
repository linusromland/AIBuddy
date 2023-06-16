import os
from discord import Client, Intents,  Message, Object, app_commands
from commands.index import register_commands

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')

intents = Intents.default()
intents.message_content = True

client = Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready() -> None:
    await tree.sync(guild=Object(GUILD_ID if GUILD_ID else ""))
    print(
        f"Logged in as {client.user.name if client.user else 'N/A'} (ID: {client.user.id if client.user else 'N/A'})")


@client.event
async def on_message(message: Message) -> None:
    print(f"{message.author}: {message.content}")

# Register all commands
register_commands(tree)


def main():
    if not DISCORD_TOKEN:
        print('Please set the DISCORD_TOKEN environment variable.')
        return

    client.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
