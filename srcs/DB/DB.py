import pickle

class DB:
	__user_data = []

	def __init__(self):
		with open("srcs/DB/user_data.pickle", "rb") as fr:
			DB.__user_data = pickle.load(fr)
			fr.close()

	@staticmethod
	def get_user_data(self):
		return DB.__user_data

	@staticmethod
	def	add_user_data(self, user_data):
		DB.__user_data.append(user_data)
		with open("srcs/DB/user_data.pickle", "wb") as fw:
			pickle.dump(DB.__db, fw)
			fw.close()