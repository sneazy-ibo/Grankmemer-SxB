from discord.message import send_message, retreive_message
from discord.button import interact_button
from utils.logger import log
from time import time, sleep
from sys import exc_info
from utils.shared import data

def lottery(username, channel_id, token, config, user_id, session_id):
	send_message(channel_id, token, config, username, "pls lottery")

	latest_message = retreive_message(channel_id, token, config, username, "pls lottery", user_id)

	if latest_message is None:
		return
	
	interact_button(channel_id, token, config, username, "pls lottery", latest_message["components"][0]["components"][-1]["custom_id"], latest_message, session_id)

def lottery_parent(username, channel_id, token, config, user_id, session_id):
	while True:
		while not data[channel_id]:
			pass

		data[channel_id] = False

		start = time()

		try:
			lottery(username, channel_id, token, config, user_id, session_id)
		except Exception:
			log(username, "WARNING", f"An unexpected error occured during the running of the `pls lottery` command: `{exc_info()}`")

		end = time()   
		
		data[channel_id] = True
		
		cooldown = config["lottery"]["cooldown"] - (end - start)

		if cooldown > 0:
			sleep(cooldown)