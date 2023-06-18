class UserData:
	def __init__(self, personal_information):
		self.__personal_information = personal_information
		self.__progress = None

	def __del__(self):
		pass

	def get_personal_information(self):
		return self.__personal_information

	def get_progress(self):
		return self.__progress

	def	get_identity(self):
		return self.__personal_information.get_identity()
	
	def	get_password(self):
		return self.__personal_information.get_password()

	def	get_name(self):
		return self.__personal_information.get_name()

	def	get_phone_number(self):
		return self.__personal_information.get_phone_number()

	def get_account_type(self):
		return self.__personal_information.get_account_type()

	def set_progress(self, progress):
		self.__progress = progress