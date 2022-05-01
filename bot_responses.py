import random

no = [
	"no",
	"No!",
	"NO!!!!!",
	"nO",
	"NO",
	"nO!!"
]

yesican = [
	"yes",
	"yes.",
	"I can do that",
	"yes!"
]

yesiwill = [
	"yes, I will",
	"yes",
	"I will",
	"yes, that is true"
]

everything = [
	"everything."
]

maybe = [
	"maybe"
]

rickroll = [
	"http://www.mit.edu/~shint/handouts/endurance.html"
]

cantagbot = [
	"tagbot able to"
]

twoplustwo = [
	"2 + 2 is not 4. It is 1,000,000,000."
]

async def bot_responses(self, message):
	# responses::twoplustwo

	if "2+2" in message.content.lower().replace(" ", ""):
		print("[responses] Running responses::twoplustwo")
		await message.reply(random.choice(twoplustwo), mention_author=True)
		return
	
	# responses::will

	if "will tagbot" in message.content.lower():
		print("[responses] Running responses::will")
		await message.reply(random.choice(yesiwill), mention_author=True)
		return

	# responses::what
		
	if "what can tagbot" in message.content.lower() or "what tagbot can" in message.content.lower():
		print("[responses] Running responses::what")
		await message.reply(random.choice(everything), mention_author=True)
		return

	# responses::can

	if "can tagbot" in message.content.lower() or "does tagbot" in message.content.lower():
		print("[responses] Running responses::can")
		await message.reply(random.choice(yesican), mention_author=True)
		return
	
	if "will tagbot" in message.content.lower() or "when will tagbot" in message.content.lower():
		print("[responses] Running responses::can")
		await message.reply(random.choice(yesican), mention_author=True)
		return
	
	if "tagbot able to" in message.content.lower() or "tagbot be able" in message.content.lower():
		print("[responses] Running responses::can")
		await message.reply(random.choice(yesican), mention_author=True)
		return