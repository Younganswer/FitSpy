import os
import sys
import random

from DB.DB import DB


class Matching:
	def __init__(self):
		pass

	@staticmethod
	def matching_trainer():
		user_data = DB.get_user_data()
		trainer_list = []
		for user in user_data:
			if user.get_account_type() == "trainer":
				trainer_list.append(user)
		return random.choice(trainer_list)
