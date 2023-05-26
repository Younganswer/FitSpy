import pickle

class DB:
	__user_data = []

	def __init__(self):
		try:
			with open("srcs/DB/user_data.pickle", "rb") as fr:
				DB.__user_data = pickle.load(fr)
				fr.close()
		except:
			pass
	
	def	__del__(self):
		with open("srcs/DB/user_data.pickle", "wb") as fw:
			pickle.dump(DB.__user_data, fw)
			fw.close()

	@staticmethod
	def get_user_data():
		return DB.__user_data

	@staticmethod
	def	add_user_data(user_data):
		DB.__user_data.append(user_data)