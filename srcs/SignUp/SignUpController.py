from DB.DB import DB
from tkinter import messagebox
from UserData.UserData import UserData
from PersonalInformation.PersonalInformation import PersonalInformation

class SignUpController:
	def __init__(self):
		pass

	@staticmethod
	def	sign_up(personal_information):
		if (
			personal_information["identity"] == "" or
			personal_information["password"] == "" or
			personal_information["name"] == "" or
			personal_information["phone_number"] == "" or
			personal_information["sex"] == "" or
			personal_information["email"] == "" or
			personal_information["account_type"] == ""
		):
			messagebox.showwarning("Warning", "Please fill in all the blanks.")
			return

		if not self.__valid_id(identity):
			messagebox.showwarning("Warning", "This ID already exists.")
			return
		
		if not self.__already_exist(name, phone_number):
			messagebox.showwarning("Warning", "Account already exists.")
			return

		self.__add_user_data(personal_information)

	def	__valid_id(self, identity):
		db = DB()
		user_data = db.get_user_data()
		for user in user_data:
			if user.get_identity() == identity:
				return False
		return True
	
	def	__already_exist(self, name, phone_number):
		db = DB()
		user_data = db.get_user_data()
		for user in user_data:
			if user.get_name() == name and user.get_phone_number() == phone_number:
				return False
		return True
	
	def	__add_user_data(self, personal_information):
		db = DB()
		db.add_user_data(
			UserData(
				PersonalInformation(
					identity=personal_information["identity"],
					password=personal_information["password"],
					name=personal_information["name"],
					phone_number=personal_information["phone_number"],
					sex=personal_information["sex"],
					email=personal_information["email"],
					account_type=personal_information["account_type"]
				)
			)
		)
		db.set_user_data(user_data)
		messagebox.showinfo("Success", "Sign Up Success!")