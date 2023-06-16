import os
from discord import Client, Intents, Interaction, Message, Object, app_commands

# Read your API keys from environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')

# Initialize your bot with the needed intents
intents = Intents.default()
intents.message_content = True

client = Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync(guild=Object(GUILD_ID if GUILD_ID else ""))
    print(
        f"Logged in as {client.user.name if client.user else 'N/A'} (ID: {client.user.id if client.user else 'N/A'})")


@client.event
async def on_message(message: Message):
    print(f"{message.author}: {message.content}")


@tree.command(name="ping", description="Ping the bot", guild=Object(GUILD_ID) if GUILD_ID else None)
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong!")


def main():
    if not DISCORD_TOKEN:
        print('Please set the DISCORD_TOKEN environment variable.')
        return

    client.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
