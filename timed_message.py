import discord
from datetime import datetime

client = discord.Client()
token = "MTM1MzkwMTQzNDU5MjE3MDExOA.GwgvnH.kvo9vaGS3UYM_I2dd4h-CD-nVWBHYZPjikwfVY" #enter your bot's token and it should be a string
channel_id = 1339429895889223773

def time_module():
    print("time module in use")
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == "21:35": 
            print("time module ended")
            break

time_module()

@client.event
async def on_ready():

    print("bot:user ready == {0.user}".format(client))
    channel = client.get_channel(channel_id)
    await channel.send("message")
    

client.run(token)