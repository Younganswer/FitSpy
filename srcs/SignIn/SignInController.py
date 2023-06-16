from DB.DB import DB
from tkinter import messagebox

class SignInController:
	def __init__(self):
		pass

	@staticmethod
	def	get_user_data(identity, password):
		if identity == "" or password == "":
			messagebox.showerror("Error", "Please fill in all fields")
			return None
		
		db = DB()
		user_data = db.get_user_data()

		for user in user_data:
			if user.get_identity() == identity and user.get_password() == password:
				return user
	
		messagebox.showerror("Error", "Incorrect username or password")
		return None