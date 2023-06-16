import os
from discord import Intents
from discord.ext import commands

# Read your API keys from environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize your bot with the needed intents
intents = Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(
        f"Logged in as {bot.user.name if bot.user else 'N/A'} (ID: {bot.user.id if bot.user else 'N/A'})")


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


def main():
    if not DISCORD_TOKEN:
        print('Please set the DISCORD_TOKEN environment variable.')
        return

    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
