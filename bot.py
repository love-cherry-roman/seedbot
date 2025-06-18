from discord.ext import commands
import discord
from discord.ext.commands import Bot
import asyncio
import time
import os
from discord import File
import sys
from discord.ext import tasks
import datetime
from discord import app_commands
import random
import math 
from numpy import *
import numexpr
from dotenv import load_dotenv
import base64
from requests import post, get
import json


#tokens for discord
BOT_TOKEN = "MTM1MzkwMTQzNDU5MjE3MDExOA.GaRnHh.7nlYLHQ9kjGS_9G_per3WFds3khYRJsLmsWxyk"
CHANNEL_ID = 1353875799262105652

#bot pre-command
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

#get the spotify id things from ythe other fle
load_dotenv()
client_id = os.getenv("S_CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#get spotify api token
def get_token():

    #mish mashing my strings together for requesting
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    #i think this is where im shipping it off to
    url = "https://accounts.spotify.com/api/token"

    #extra info
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    #give me ur data spotify
    data = {"grant_type": "client_credentials"}

    #send it off, post at the url
    result = post(url, headers=headers, data=data)

    #puts the content neatly in json
    json_result = json.loads(result.content)

    #give me the token specifically
    token = json_result["access_token"]

    #you know
    return token


def get_auth_headers(token):

    #give access to whoever has this token
    return {"Authorization": "Bearer " + token}


def search_for_track(token, track_name):

    #use this to search
    url = "https://api.spotify.com/v1/search"

    #YOU get the token
    headers = get_auth_headers(token)

    #i want the most populat (&limit=1) track
    query = f"q={track_name}&type=track&limit=1"

    #add this to that url top search
    query_url= url + "?" + query

    #yurp
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    if len(json_result) == 0:
        print("No track with this name exists...")
        return None
    


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"

    #your turn w/ the token
    headers = get_auth_headers(token)

    #I want artists this time
    query = f"?q={artist_name}&type=artist&limit=1"

    #I put the question mark in the original query haha
    query_url= url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("Fake artist")
        return None
    return json_result[0]


@bot.command()
async def searchforsong(ctx, track_name):
    token = get_token()
    result = search_for_track(token, track_name)
    songid = result["id"]
    await ctx.send("http" + "s://open.spotify.com/track/" + songid)


@bot.command()
async def searchforartist(ctx, artist_name):
    token = get_token()  
    result = search_for_artist(token, artist_name)
    artistid = result["id"]
    await ctx.send("http" + "s://open.spotify.com/artist/" + artistid)


@bot.command()
async def toptracks(ctx, artist_name):
    token= get_token()
    result = search_for_artist(token, artist_name)
    artist_id = result["id"]
    songs = get_songs_by_artist(token, artist_id)
    for idx, song in enumerate(songs):
        listthing = await ctx.send(str(f"{idx +1}. {song['name']}"))


def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?"
    headers = get_auth_headers(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

#testing stuff
token= get_token()
result = search_for_artist(token, "seedbean")
artist_id = result["id"]
songs = get_songs_by_artist(token, artist_id)
#ok im done


@bot.command()
#I wonder
async def hello(ctx):
    await ctx.send("Hi")


@bot.command()
async def idplma(ctx):
    #i dont want to type the file name
    audio = "ID3"
    file = File(audio)

    #It made me write it liek this idk why
    await ctx.send(file = file)


@bot.command(aliases=["calc", "solve"])

#thank you numexpr
async def calculate(ctx, *, expression: str):
    try:
        answer = numexpr.evaluate(expression)

        #f string aka fancy string
        await ctx.send(f"{expression} = {answer}")
    except:
        await ctx.send("your stupid problem is wrong")


@bot.command()
async def crack(ctx):
    #random list that i somehow made work
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
#does literally nothing
async def quit(ctx):
    sys.exit()


@bot.event
async def on_ready():
    #just making sure it works
    print("hi")
    channel = bot.get_channel(CHANNEL_ID)

bot.run(BOT_TOKEN) #!important
#get it because it looks like css but it isnt