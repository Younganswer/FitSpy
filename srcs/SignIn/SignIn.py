import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from SignIn.SignInController import SignInController


class SignIn(tk.Frame):
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
		self.__set_buttons()

	def __set_title(self):
		self.__title = ttk.Label(self, text="Fitspy", font=("Helvetica", 30))
		self.__title.place(x=180, y=160, anchor="center")

	def __set_labels(self):
		self.__identity_label = ttk.Label(self, text="ID")
		self.__password_label = ttk.Label(self, text="Password")
		self.__identity_label.place(x=90, y=290, width=90, height=20, anchor="center")
		self.__password_label.place(x=90, y=320, width=90, height=20, anchor="center")

	def __set_entries(self):
		self.__identity = ttk.Entry(self, font=("Helvetica", 10))
		self.__password = ttk.Entry(self, font=("Helvetica", 10), show="*")
		self.__identity.place(x=225, y=290, width=180, height=20, anchor="center")
		self.__password.place(x=225, y=320, width=180, height=20, anchor="center")

	def __set_buttons(self):
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
			command=self.__signIn,
			style="RoundedButton.TButton",
		)
		self.__sign_up_button = ttk.Button(
			self,
			text="Sign Up",
			command=lambda: self.__controller.show_frame("SignUp"),
			style="RoundedButton.TButton",
		)
		self.__sign_in_button.place(x=180, y=370, width=270, height=25, anchor="center")
		self.__sign_up_button.place(x=180, y=405, width=270, height=25, anchor="center")

	# Sign in
	def __signIn(self):
		# Get username and password
		identity = self.__identity.get()
		password = self.__password.get()

		# Check if username and password are empty
		if identity == "" or password == "":
			messagebox.showerror("Error", "Please fill in all fields")
			return

		# Check if username and password are correct
		if SignInController.validate(identity, password):
			self.__identity.delete(0, tk.END)
			self.__password.delete(0, tk.END)
			# Get user data
			self.__controller.show_frame("TraineeHome")
		else:
			messagebox.showerror("Error", "Incorrect username or password")
			return