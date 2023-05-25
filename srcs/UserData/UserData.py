class UserData:
	def __init__(self, personal_information):
		self.__personal_information = personal_information
		self.__progresses = []

	def __del__(self):
		pass

	def get_personal_information(self):
		return self.__personal_information

	def get_progress(self):
		return self.__progresses

	def append_progress(self, progress):
		self.__progresses.append(progress)

	def get_account_type(self):
		return self.__personal_information.get_account_type()