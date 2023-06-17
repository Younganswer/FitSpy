from DB.DB import DB
from tkinter import messagebox

class SignInController:
	def __new__(cls, *args, **kwargs):
		raise TypeError("Static class 'SignInController' cannot be instantiated")

	@staticmethod
	def	get_user_data(identity, password):
		if identity == "" or password == "":
			messagebox.showerror("Error", "Please fill in all fields")
			return None
		
		db = DB()
		users_data_by_id = db.get_users_data_by_id()
		user = None

		try:
			user = users_data_by_id[identity]
		except:
			messagebox.showerror("Error", "Incorrect username or password")

		if user.get_password() != password:
			messagebox.showerror("Error", "Incorrect username or password")
			return None
		return user