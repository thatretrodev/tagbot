from bot_responses import *
import random

counters = {"no": 0}

async def bot_no(self, message):
	if "no" in message.content.lower().replace("0", "o"):
			if "not" in message.content.lower() or "now" in message.content.lower():
				return
			
			if counters["no"] > 50:
				return

			# This is very fun. You should include it in all of your Discord bots.

			if random.randint(1, 100) == 1 and str(message.author) != "thatretrodev#3049":
				# no::rickroll
				
				print("[no] Running no::rickroll")
				await message.reply(random.choice(rickroll), mention_author=True)
				return

			# no::no
			
			print("[no] Running no::no")
			counters["no"] += 1
			#print(counters["no"], message.content)
			await message.reply(random.choice(no), mention_author=True)
			return
