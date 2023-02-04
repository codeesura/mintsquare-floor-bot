import discord
from discord.ext import commands , tasks
import requests
import json
import asyncio
import time
from datetime import datetime
from web3 import Web3

intents = discord.Intents.default()
client = commands.Bot(command_prefix = '$',intents=intents)

nft_contract_address = "0x01c7607659020c0f128fe677a1d7be9c3b9f66cedfe50296aca146b003875ee5"

@tasks.loop(seconds=15)
async def status_task():
        try:
            getir = requests.get(f"https://api.mintsquare.io/v0/collection/starknet-mainnet/{nft_contract_address}/").text            
            getir = json.loads(getir)
            getir_usd = int(getir["stats"]["floor_price"])
            for guild in client.guilds:
                    await guild.me.edit(nick=f"{round(Web3.fromWei(getir_usd,'ether'),3)} Ξ")
        except : pass

@client.command()
async def server_info(ctx):
    for guild in client.guilds:
        await ctx.send(guild)

@client.event
async def on_ready():
    await client.wait_until_ready()   
    status_task.start()
    print('bot ready!! !')

client.run("TOKEN")
