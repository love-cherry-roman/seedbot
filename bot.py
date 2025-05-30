from discord.ext import commands
import discord
from discord.ext.commands import Bot
import asyncio
import time
from discord import File
import sys
from discord.ext import tasks
import datetime
from discord import app_commands
import random
import math 
import os
from discord.ext import commands
from datetime import datetime, time, timedelta
import asyncio




BOT_TOKEN = "MTM1MzkwMTQzNDU5MjE3MDExOA.GwgvnH.kvo9vaGS3UYM_I2dd4h-CD-nVWBHYZPjikwfVY"
CHANNEL_ID = 1353875799262105652

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

from keep_alive import keep_alive

keep_alive()

@bot.command()
async def hello(ctx):
    await ctx.send("Hi")

@bot.command()
async def help(ctx):
    await ctx.send("List of all commands:")

@bot.command()
async def idplma(ctx):
    audio = "ID3"
    file = File(audio)
    await ctx.send(file = file)

@bot.command()
async def add(ctx, *arr):
    result = 0
    for i in arr:
        result += int(i)

    await ctx.send(f"Result: {result}")

@bot.command()
async def subtract(ctx, *arr):
    result = 0
    for i in arr:
        result -= int(i)

    await ctx.send(f"Result: {result}")

@bot.command()
async def multiply(ctx, *arr):
    result = 1
    for i in arr:
        result *= int(i)
    await ctx.send(f"Result: {result}")

@bot.command()
async def divide(ctx, *arr):
    result = 1
    for i in arr:
        result /= int(i)
    await ctx.send(f"Result: {result}")


@bot.command()
async def crack(ctx):
    msg_list_crack = ["oh yeah", "that gets me wired", "thats the good stuff", "yesss give me more"]
    await ctx.send(random.choice(msg_list_crack))

@bot.command()
async def hit(ctx):
    msg_list_hurt = ["ow", "ouch", "owie", "ow stop", "owwwwwW"]
    await ctx.send(random.choice(msg_list_hurt))

@bot.command()
async def seedbean(ctx):
    image = "seedbean.jpg"
    file = File(image)
    await ctx.send(file = file)


@bot.command()
async def quit(ctx):
    sys.exit()



async def main():
    async with bot:
        await bot.start(BOT_TOKEN)


asyncio.run(main())
