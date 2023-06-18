class UserDataController:
	__instance = None
	__user_data = None

	def __new__(cls):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
		return cls.__instance

	def get_user_data(self):
		return UserDataController.__user_data

	def set_user_data(self, user_data):
		UserDataController.__user_data = user_data