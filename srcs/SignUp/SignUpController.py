from DB.DB import DB
from tkinter import messagebox
from UserData.UserData import UserData
from PersonalInformation.PersonalInformation import PersonalInformation

class SignUpController:
	def __new__(cls, *args, **kwargs):
		raise TypeError("Static class 'SignUpController' cannot be instantiated")

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

		if SignUpController.__already_exist_id(personal_information["identity"]):
			messagebox.showwarning("Warning", "This ID already exists.")
			return
		
		if SignUpController.__already_own_account(personal_information["phone_number"]):
			messagebox.showwarning("Warning", "You already own an account.")
			return

		SignUpController.__add_user_data(personal_information)

	@staticmethod
	def	__already_exist_id(identity):
		db = DB()
		users_data_by_id = db.get_users_data_by_id()
		try:
			users_data_by_id[identity]
		except:
			return False
		return True
	
	@staticmethod
	def	__already_own_account(phone_number):
		db = DB()
		users_data_by_phone_number = db.get_users_data_by_phone_number()
		try:
			users_data_by_phone_number[phone_number]
		except:
			return False
		return True
	
	@staticmethod
	def	__add_user_data(personal_information):
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
		messagebox.showinfo("Success", "Sign Up Success!")