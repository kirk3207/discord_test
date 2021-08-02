import discord
from discord.ext import commmands

bot = commands.Bot(command_prefix = '@xi')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('ODcxNzI2NjI1MTcwMDMwNjYz.YQfgrw.E1mpYHrz8-n8aROG6CeN7EqizmM')