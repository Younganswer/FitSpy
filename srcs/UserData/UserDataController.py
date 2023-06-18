class UserDataController:
	__instance = None
	__cur_user_data = None

	def __new__(cls):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
		return cls.__instance

	def get_cur_user_data(self):
		return UserDataController.__cur_user_data

	def set_cur_user_data(self, user_data):
		UserDataController.__cur_user_data = user_data