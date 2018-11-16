import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from os import path






client = discord.Client()
Client = Bot(command_prefix=["each."])


#----------------In developpement-------------------------


@client.event
async def on_ready():
	print("																											")
	print("	.▄▄ · ▄▄▄ .▄▄▌  ·▄▄▄▄▄▄▄·       ▄▄▄▄▄    ▄▄▄ . ▄▄▄· .▄▄▄  ▄• ▄▌▄▄▄ ..▄▄ · ▄▄▄▄▄ ▄▄▄·  ▄▄· ▄ •▄ .▄▄ · 	")
	print("	▐█ ▀. ▀▄.▀·██•  ▐▄▄·▐█ ▀█▪▪     •██      ▀▄.▀·▐█ ▀█ ▐▀•▀█ █▪██▌▀▄.▀·▐█ ▀. •██  ▐█ ▀█ ▐█ ▌▪█▌▄▌▪▐█ ▀. 	")
	print("	▄▀▀▀█▄▐▀▀▪▄██▪  ██▪ ▐█▀▀█▄ ▄█▀▄  ▐█.▪    ▐▀▀▪▄▄█▀▀█ █▌·.█▌█▌▐█▌▐▀▀▪▄▄▀▀▀█▄ ▐█.▪▄█▀▀█ ██ ▄▄▐▀▀▄·▄▀▀▀█▄	")
	print("	▐█▄▪▐█▐█▄▄▌▐█▌▐▌██▌.██▄▪▐█▐█▌.▐▌ ▐█▌·    ▐█▄▄▌▐█ ▪▐▌▐█▪▄█·▐█▄█▌▐█▄▄▌▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐███▌▐█.█▌▐█▄▪▐█	")
	print("	 ▀▀▀▀  ▀▀▀ .▀▀▀ ▀▀▀ ·▀▀▀▀  ▀█▄▀▪ ▀▀▀      ▀▀▀  ▀  ▀ ·▀▀█.  ▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀  ▀  ▀ ·▀▀▀ ·▀  ▀ ▀▀▀▀ 	")
	print("\n")
	print("client disconnect: \n")
	print("\n")
	print("client online:\n")
	print(client.user.name+"\n")
	print("Bot Dev by Eaque")

@client.event
async def on_message(message):


client.run("XXXXXXXXXXXXXXXXXXXX", bot=False)

