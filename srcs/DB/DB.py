import pickle

def	init_user_data():
	try:
		with open("DB/user_data.pickle", "rb") as f:
			user_data = pickle.load(f)
	except FileNotFoundError:
		user_data = []
	return user_data

class DB:
	__user_data = init_user_data()

	@staticmethod
	def get_user_data():
		return DB.__user_data

	@staticmethod
	def	add_user_data(user_data):
		DB.__user_data.append(user_data)
		with open("DB/user_data.pickle", "wb") as f:
			pickle.dump(DB.__user_data, f)