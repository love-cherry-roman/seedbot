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



banned_words = ["FUCK", "STUPID", "FAT", "fuck", "stupid", "fat"]

WHEN = time(20, 45, 0)  # 6:00 PM
channel_id = 1339429895889223773

async def called_once_a_day():
    await bot.wait_until_ready()  # Make sure your guild cache is ready so the channel can be found via get_channel
    channel = bot.get_channel(channel_id) # Note: It's more efficient to do bot.get_guild(guild_id).get_channel(channel_id) as there's less looping involved, but just get_channel still works fine
    await channel.send("hi(it worked)")

async def background_task():
    now = datetime.utcnow()
    if now.time() > WHEN:  # Make sure loop doesn't start after {WHEN} as then it will send immediately the first time as negative seconds will make the sleep yield instantly
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
        await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start 
    while True:
        now = datetime.utcnow() # You can do now() or a specific timezone if that matters, but I'll leave it with utcnow
        target_time = datetime.combine(now.date(), WHEN)  # 6:00 PM today (In UTC)
        seconds_until_target = (target_time - now).total_seconds()
        await asyncio.sleep(seconds_until_target)  # Sleep until we hit the target time
        await called_once_a_day()  # Call the helper function that sends the message
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
        await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start a new iteration



@bot.command()
async def hello(ctx):
    await ctx.send("Hi")

async def hello(ctx):
    await ctx.send("Hi")

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

