import os
import sys
import random

from DB.DB import DB

class TheMostAdvancedAIWithTheLatestTechnology:
	def __init__(self):
		pass

	@staticmethod
	def matching_trainer():
		db = DB()
		users_data = db.get_users_data()
		trainer_list = []
		for user in users_data:
			if user.get_account_type() == "Trainer":
				trainer_list.append(user)
		if len(trainer_list) == 0:
			raise Exception("TheMostAdvancedAIWithTheLatestTechnology: There is no trainer.")
		return random.choice(trainer_list)
