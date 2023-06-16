import tkinter as tk
from tkinter import ttk
from Page.Page import APage
from SignIn.SignInController import SignInController

class SignIn(APage):
	def __init__(self, parent, controller):
		super().__init__(parent, controller)
		self._set_page()

	def __del__(self):
		pass

	def	_set_page(self):
		self._set_widgets()
		self._set_title()
		self._set_labels()
		self._set_entries()
		self._set_buttons()

	def _set_widgets(self):
		self._set_title()
		self._set_labels()
		self._set_entries()
		self._set_buttons()

	def _set_title(self):
		self.__title = ttk.Label(self, text="Fitspy", font=("Helvetica", 30))
		self.__title.place(x=180, y=200, anchor="center")

	def _set_labels(self):
		self.__identity_label = ttk.Label(self, text="ID")
		self.__password_label = ttk.Label(self, text="Password")
		self.__identity_label.place(x=90, y=320, width=90, height=20, anchor="center")
		self.__password_label.place(x=90, y=350, width=90, height=20, anchor="center")

	def _set_entries(self):
		self.__identity = ttk.Entry(self, font=("Helvetica", 10))
		self.__password = ttk.Entry(self, font=("Helvetica", 10), show="*")
		self.__identity.place(x=225, y=320, width=180, height=20, anchor="center")
		self.__password.place(x=225, y=350, width=180, height=20, anchor="center")

	def _set_buttons(self):
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

		self.__sign_in_button = ttk.Button(
			self,
			text="Sign In",
			command=self.__sign_in,
			style="RoundedButton.TButton",
		)
		self.__sign_up_button = ttk.Button(
			self,
			text="Sign Up",
			command=lambda: self._controller.show_frame("SignUp"),
			style="RoundedButton.TButton",
		)
		self.__sign_in_button.place(x=180, y=400, width=270, height=25, anchor="center")
		self.__sign_up_button.place(x=180, y=435, width=270, height=25, anchor="center")

	def __sign_in(self):
		identity = self.__identity.get()
		password = self.__password.get()

		user = SignInController.get_user_data(identity, password)
		if user is not None:
			self.__identity.delete(0, tk.END)
			self.__password.delete(0, tk.END)
			if user.get_account_type() == "Trainee":
				self._controller.show_frame("TraineeHome")
			else:
				self._controller.show_frame("TrainerHome")