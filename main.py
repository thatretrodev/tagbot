from dotenv import load_dotenv
from bot_responses import *
from bot_food import *
from bot_no import *
import disnake
import random
import os

load_dotenv()

class TagbotClient(disnake.Client):
	async def on_ready(self):
		print(f"Logged in as {self.user} (ID: {self.user.id})")
		#print("------")

	async def on_message(self, message):
		# we do not want the bot to reply to itself
		if message.author.id == self.user.id:
			return

		#print(message.author)

		await bot_no(self, message)
		await bot_food(self, message)
		await bot_responses(self, message)

	

client = TagbotClient()
client.run(os.environ["BOT_TOKEN"])