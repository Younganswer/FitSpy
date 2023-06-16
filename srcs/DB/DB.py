import pickle

def _init_user_data():
	try:
		with open("srcs/DB/user_data.pickle", "rb") as f:
			user_data = pickle.load(f)
	except FileNotFoundError or IOError:
		user_data = []
	return user_data

# Pure fabrication
# Singleton pattern
# Information expert principle
class DB:
	__instance = None  # Singleton instance
	__user_data = _init_user_data()

	# Get singleton instance
	def __new__(cls):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
		return cls.__instance

	def get_user_data(self):
		return DB.__user_data

	def add_user_data(self, user_data):
		DB.__user_data.append(user_data)
		try:
			with open("srcs/DB/user_data.pickle", "wb") as f:
				pickle.dump(DB.__user_data, f)
		except FileNotFoundError:
			print("Error: DB: File not found.")
		except IOError:
			print("Error: DB: IOError.")