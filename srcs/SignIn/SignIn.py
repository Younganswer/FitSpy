import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from SignIn.SignInController import SignInController


class SignIn(tk.Frame):
	def __init__(self, parent, controller):
		super().__init__(parent)
		self.__controller = controller
		self.__setWidgets()
		self.__show()

	def __del__(self):
		pass

	def __setWidgets(self):
		self.__setGridConfigure()
		self.__setTitle()
		self.__setLabels()
		self.__setEntries()
		self.__setButtons()

	def __setGridConfigure(self):
		self.grid_rowconfigure(0, minsize=180)
		self.grid_rowconfigure(1, minsize=50)
		self.grid_rowconfigure(2, minsize=65)
		self.grid_rowconfigure(3, minsize=20)
		self.grid_rowconfigure(4, minsize=20)
		self.grid_rowconfigure(5, minsize=10)
		self.grid_rowconfigure(6, minsize=20)
		self.grid_rowconfigure(7, minsize=20)
		self.grid_rowconfigure(8, minsize=255)
		self.grid_columnconfigure(0, minsize=45)
		self.grid_columnconfigure(1, minsize=90)
		self.grid_columnconfigure(2, minsize=180)
		self.grid_columnconfigure(3, minsize=45)

	def __setTitle(self):
		self.__title = ttk.Label(self, text="Fitspy", font=("Helvetica", 30))
		self.__title.grid(row=1, column=1, columnspan=2)

	def __setLabels(self):
		self.__identityLabel = ttk.Label(self, text="ID")
		self.__passwordLabel = ttk.Label(self, text="Password")
		self.__identityLabel.grid(row=3, column=1, pady=5)
		self.__passwordLabel.grid(row=4, column=1, pady=5)

	def __setEntries(self):
		self.__identity = ttk.Entry(self, font=("Helvetica", 10))
		self.__password = ttk.Entry(self, font=("Helvetica", 10), show="*")
		self.__identity.grid(row=3, column=2, pady=5)
		self.__password.grid(row=4, column=2, pady=5)

	def __setButtons(self):
		style = ttk.Style()
		style.configure("RoundedButton.TButton",
						borderwidth=0,
						relief="flat",
						background="#c9c9c9",
						foreground="black",
						font=("Helvetica", 10))
		style.map("RoundedButton.TButton", background=[("active", "#a9a9a9")])
		self.__signInButton = ttk.Button(self,
										 text="Sign In",
										 command=self.__signIn,
										 style="RoundedButton.TButton")
		self.__signInButton.grid(row=6,
								 column=1,
								 pady=5,
								 columnspan=2,
								 sticky=tk.W + tk.E)

		self.__signUpButton = ttk.Button(self,
										 text="Sign Up",
										 command=lambda: self.__controller.showFrame("SignUp"),
										 style="RoundedButton.TButton")
		self.__signUpButton.grid(row=7,
								 column=1,
								 pady=5,
								 columnspan=2,
								 sticky=tk.W + tk.E)

	def __show(self):
		self.pack(fill=tk.BOTH, expand=True)

	# Sign in
	def __signIn(self):
		# Get username and password
		identity = self.__identity.get()
		password = self.__password.get()

		# Check if username and password are empty
		if (identity == "" or password == ""):
			messagebox.showerror("Error", "Please fill in all fields")
			return

		# Check if username and password are correct
		if (SignInController.validate(identity, password)):
			self.__identity.delete(0, tk.END)
			self.__password.delete(0, tk.END)
			self.__controller.showFrame("Home")
		else:
			messagebox.showerror("Error", "Incorrect username or password")
			return
