class PersonalInformation:
	def __init__(self, identity, password, name, phone_number, sex, email, account_type):
		self.__identity = identity
		self.__password = password
		self.__name = name
		self.__phone_number = phone_number
		self.__sex = sex
		self.__email = email
		self.__account_type = account_type

	def get_name(self):
		return self.__name

	def get_phone_number(self):
		return self.__phone_number

	def get_sex(self):
		return self.__sex

	def get_email(self):
		return self.__email

	def get_account_type(self):
		return self.__account_type

	def get_identity(self):
		return self.__identity

	def get_password(self):
		return self.__password

	def set_email(self, email):
		self.__email = email

	def set_password(self, password):
		self.__password = password
