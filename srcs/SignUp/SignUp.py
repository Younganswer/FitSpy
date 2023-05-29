import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from DB.DB import DB
from UserData.UserData import UserData
from PersonalInformation.PersonalInformation import PersonalInformation


class SignUp(tk.Frame):
	def __init__(self, parent, controller):
		super().__init__(parent)
		self.__controller = controller
		self.__set_widgets()

	def __del__(self):
		pass

	def __set_widgets(self):
		self.__set_title()
		self.__set_labels()
		self.__set_entries()
		self.__set_button()

	def __set_title(self):
		self.__title = ttk.Label(self, text="Fitspy", font=("Helvetica", 30))
		self.__title.place(x=180, y=120, anchor="center")

	def __set_labels(self):
		self.__identity_label = ttk.Label(self, text="ID")
		self.__password_label = ttk.Label(self, text="Password")
		self.__name_label = ttk.Label(self, text="Name")
		self.__phone_number_label = ttk.Label(self, text="Phone Number")
		self.__sex_label = ttk.Label(self, text="Sex")
		self.__email_label = ttk.Label(self, text="Email")
		self.__account_type_label = ttk.Label(self, text="Account Type")
		self.__identity_label.place(x=100, y=230, width=110, height=20, anchor="center")
		self.__password_label.place(x=100, y=260, width=110, height=20, anchor="center")
		self.__name_label.place(x=100, y=290, width=110, height=20, anchor="center")
		self.__phone_number_label.place(
			x=100, y=320, width=110, height=20, anchor="center"
		)
		self.__sex_label.place(x=100, y=350, width=110, height=20, anchor="center")
		self.__email_label.place(x=100, y=380, width=110, height=20, anchor="center")
		self.__account_type_label.place(
			x=100, y=410, width=110, height=20, anchor="center"
		)

	def __set_entries(self):
		self.__identity = ttk.Entry(self, font=("Helvetica", 10))
		self.__password = ttk.Entry(self, font=("Helvetica", 10), show="*")
		self.__name = ttk.Entry(self, font=("Helvetica", 10))
		self.__phone_number = ttk.Entry(self, font=("Helvetica", 10))
		self.__sex = ttk.Combobox(
			self,
			font=("Helvetica", 10),
			state="readonly",
			textvariable=tk.StringVar(),
			values=["Male", "Female"],
			background="lightgray",
		)
		self.__email = ttk.Entry(self, font=("Helvetica", 10))
		self.__account_type = ttk.Combobox(
			self,
			font=("Helvetica", 10),
			state="readonly",
			textvariable=tk.StringVar(),
			values=["Trainee", "Trainer"],
			background="lightgray",
		)
		self.__identity.place(x=235, y=230, width=160, height=20, anchor="center")
		self.__password.place(x=235, y=260, width=160, height=20, anchor="center")
		self.__name.place(x=235, y=290, width=160, height=20, anchor="center")
		self.__phone_number.place(x=235, y=320, width=160, height=20, anchor="center")
		self.__sex.place(x=235, y=350, width=160, height=20, anchor="center")
		self.__email.place(x=235, y=380, width=160, height=20, anchor="center")
		self.__account_type.place(x=235, y=410, width=160, height=20, anchor="center")

	def __set_button(self):
		style = ttk.Style()
		style.configure(
			"RoundedButton.TButton",
			borderwidth=0,
			relief="flat",
			background="#c9c9c9",
			foreground="black",
			font=("Helvetica", 10),
		)
		style.map("RoundedButton.TButton", background=[("active", "#a9a9a9")])

		self.__sign_up_button = ttk.Button(
			self, text="Sign Up", style="RoundedButton.TButton", command=self.__sign_up
		)
		self.__sign_up_button.place(x=180, y=450, width=270, height=30, anchor="center")

	def __sign_up(self):
		identity = self.__identity.get()
		password = self.__password.get()
		name = self.__name.get()
		phone_number = self.__phone_number.get()
		sex = self.__sex.get()
		email = self.__email.get()
		account_type = self.__account_type.get()

		if (
			identity == ""
			or password == ""
			or name == ""
			or phone_number == ""
			or sex == ""
			or email == ""
			or account_type == ""
		):
			messagebox.showwarning("Warning", "Please fill in all the blanks.")
			return

		if not self.__valid_id(identity):
			messagebox.showwarning("Warning", "This ID already exists.")
			return
		
		if not self.__already_exist(name, phone_number):
			messagebox.showwarning("Warning", "Account already exists.")
			return

		DB.add_user_data(
			UserData(
				PersonalInformation(
					name,
					phone_number,
					sex,
					email,
					account_type,
					identity,
					password,
				)
			)
		)
		messagebox.showinfo("Success", "Sign Up Success!")
	
	def	__valid_id(self, identity):
		user_data = DB.get_user_data()
		for user in user_data:
			if user.get_identity() == identity:
				return False
		return True
	
	def	__already_exist(self, name, phone_number):
		user_data = DB.get_user_data()
		for user in user_data:
			if user.get_name() == name and user.get_phone_number() == phone_number:
				return False
		return True
