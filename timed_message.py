import discord
from datetime import datetime
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

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())
token = "MTM1MzkwMTQzNDU5MjE3MDExOA.GaRnHh.7nlYLHQ9kjGS_9G_per3WFds3khYRJsLmsWxyk" #enter your bot's token and it should be a string
channel_id = 1353875799262105652

def time_module():
    print("time module in use")
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == "22:32": 
            print("time module ended")

time_module()

@client.event
async def on_ready():

    print("bot:user ready == {0.user}".format(client))
    channel = client.get_channel(channel_id)
    await channel.send("it it worke")
    

client.run(token)
