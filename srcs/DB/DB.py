import pickle

def _init_users_data():
	try:
		with open("srcs/DB/users_data.pickle", "rb") as f:
			users_data = pickle.load(f)
	except FileNotFoundError or IOError:
		users_data = []
	return users_data

def _init_users_data_by_id(users_data):
	users_data_by_id = {}
	for user_data in users_data:
		users_data_by_id[user_data.get_identity()] = user_data
	return users_data_by_id

def _init_users_data_by_phone_number(users_data):
	users_data_by_phone_number = {}
	for user_data in users_data:
		users_data_by_phone_number[user_data.get_phone_number()] = user_data
	return users_data_by_phone_number

# Pure fabrication
# Singleton pattern
# Information expert principle
class DB:
	__instance = None  # Singleton instance
	__users_data = _init_users_data()
	__users_data_by_id = _init_users_data_by_id(__users_data)
	__users_data_by_phone_number = _init_users_data_by_phone_number(__users_data)

	# Get singleton instance
	def __new__(cls):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
		return cls.__instance

	def get_users_data(self):
		return DB.__users_data
	
	def get_users_data_by_id(self):
		return DB.__users_data_by_id
	
	def get_users_data_by_phone_number(self):
		return DB.__users_data_by_phone_number

	def add_user_data(self, user_data):
		DB.__users_data.append(user_data)
		DB.__users_data_by_id[user_data.get_identity()] = user_data
		DB.__users_data_by_phone_number[user_data.get_phone_number()] = user_data
		try:
			with open("srcs/DB/users_data.pickle", "wb") as f:
				pickle.dump(DB.__users_data, f)
		except FileNotFoundError:
			print("Error: DB: File not found.")
		except IOError:
			print("Error: DB: IOError.")