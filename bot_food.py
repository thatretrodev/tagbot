import random

snack = [
	":croissant:",
	":pretzel:",
	":doughnut:",
	":cookie:"
]

breakfast = [
	":pancakes:",
	":waffle:",
	":bacon:"
]

lunch = [
	":poultry_leg:",
	":hotdog:",
	":hamburger:",
	":fries:",
	":pizza:",
	":sandwich:",
	":salad:",
	":spaghetti:",
	":burrito:"
]

dinner = [
	":cut_of_meat:",
	":meat_on_bone:",
	":spaghetti:",
	":pie:",
	":cake:",
	":birthday:"
]

async def bot_food(self, message):
	if ("cook" in message.content.lower() or "make" in message.content.lower()) and f"<@{self.user.id}>" in message.content:
		# food::snack

		if "snack" in message.content.lower():
			print("[food] Running food::snack")
			await message.reply(random.choice(snack), mention_author=True)
			return

		# food::breakfast
		
		if "breakfast" in message.content.lower():
			print("[food] Running food::breakfast")
			await message.reply(random.choice(breakfast), mention_author=True)
			return

		# food:lunch
		
		if "lunch" in message.content.lower():
			print("[food] Running food::lunch")
			await message.reply(random.choice(lunch), mention_author=True)
			return

		# food:dinner

		if "dinner" in message.content.lower():
			print("[food] Running food::dinner")
			await message.reply(random.choice(dinner), mention_author=True)
			return
		
		print(message.content)