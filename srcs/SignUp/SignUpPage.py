import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Page.Page import APage
from SignUp.SignUpController import SignUpController

class SignUpPage(APage):
	def __init__(self, parent, controller):
		super().__init__(parent, controller)
		self._set_widgets()

	def __del__(self):
		pass

	def	_set_widgets(self):
		self.__set_title()
		self.__set_labels()
		self.__set_entries()
		self.__set_button()

	def __set_title(self):
		self.__title = ttk.Label(self, text="Fitspy", font=("Helvetica", 30))
		self.__title.place(x=180, y=140, anchor="center")

	def __set_labels(self):
		self.__identity_label = ttk.Label(self, text="ID")
		self.__password_label = ttk.Label(self, text="Password")
		self.__name_label = ttk.Label(self, text="Name")
		self.__phone_number_label = ttk.Label(self, text="Phone Number")
		self.__sex_label = ttk.Label(self, text="Sex")
		self.__email_label = ttk.Label(self, text="Email")
		self.__account_type_label = ttk.Label(self, text="Account Type")
		self.__identity_label.place(x=100, y=250, width=110, height=20, anchor="center")
		self.__password_label.place(x=100, y=280, width=110, height=20, anchor="center")
		self.__name_label.place(x=100, y=310, width=110, height=20, anchor="center")
		self.__phone_number_label.place(
			x=100, y=340, width=110, height=20, anchor="center"
		)
		self.__sex_label.place(x=100, y=370, width=110, height=20, anchor="center")
		self.__email_label.place(x=100, y=400, width=110, height=20, anchor="center")
		self.__account_type_label.place(
			x=100, y=430, width=110, height=20, anchor="center"
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
		self.__identity.place(x=235, y=250, width=160, height=20, anchor="center")
		self.__password.place(x=235, y=280, width=160, height=20, anchor="center")
		self.__name.place(x=235, y=310, width=160, height=20, anchor="center")
		self.__phone_number.place(x=235, y=340, width=160, height=20, anchor="center")
		self.__sex.place(x=235, y=370, width=160, height=20, anchor="center")
		self.__email.place(x=235, y=400, width=160, height=20, anchor="center")
		self.__account_type.place(x=235, y=430, width=160, height=20, anchor="center")

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
		self.__sign_up_button.place(x=180, y=470, width=270, height=30, anchor="center")

	def __sign_up(self):
		personal_information = {
			"identity": self.__identity.get(),
			"password": self.__password.get(),
			"name": self.__name.get(),
			"phone_number": self.__phone_number.get(),
			"sex": self.__sex.get(),
			"email": self.__email.get(),
			"account_type": self.__account_type.get()
		}

		SignUpController.sign_up(personal_information)
		self.__show_sign_in_page()

	def	__show_sign_in_page(self):
		self.__identity.delete(0, tk.END)
		self.__password.delete(0, tk.END)	
		self.__name.delete(0, tk.END)
		self.__phone_number.delete(0, tk.END)
		self.__sex.delete(0, tk.END)
		self.__email.delete(0, tk.END)
		self.__account_type.delete(0, tk.END)
		self._controller.show_frame("SignIn")
