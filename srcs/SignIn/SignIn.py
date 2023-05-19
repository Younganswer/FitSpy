import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import SignUp.SignUp as SignUp

# SignIn class
class SignIn(tk.Frame):
	# Constructor
	def __init__(self, parent, controller):
		super().__init__(parent)
		self.__controller = controller
		self.__setGridConfigure()
		self.__createWidgets()
		self.__show()
	
	def __del__(self):
		pass

	def __setGridConfigure(self):
		self.grid_rowconfigure(0, weight=15)
		self.grid_rowconfigure(1, weight=2)
		self.grid_rowconfigure(2, weight=3)
		self.grid_rowconfigure(3, weight=1)
		self.grid_rowconfigure(4, weight=1)
		self.grid_rowconfigure(5, weight=1)
		self.grid_rowconfigure(6, weight=1)
		self.grid_rowconfigure(7, weight=20)
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=2)
		self.grid_columnconfigure(2, weight=4)
		self.grid_columnconfigure(3, weight=1)

	# Create widgets
	def __createWidgets(self):
		# Create Logo
		self.__logo = ttk.Label(self, text="Fitspy", font=("Helvetica", 30))
		self.__logo.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky=tk.N+tk.S)

		# Create Labels
		self.__identityLabel = ttk.Label(self, text="Username")
		self.__passwordLabel = ttk.Label(self, text="Password")
		self.__identityLabel.grid(row=1, column=1, padx=10, pady=10, sticky=tk.N+tk.S)
		self.__passwordLabel.grid(row=2, column=1, padx=10, pady=10, sticky=tk.N+tk.S)

		# Create Entries
		self.__identity = ttk.Entry(self)
		self.__password = ttk.Entry(self, show="*")
		self.__identity.grid(row=1, column=2, padx=10, pady=10, ipady=20, sticky=tk.N+tk.S)
		self.__password.grid(row=2, column=2, padx=10, pady=10, ipady=20, sticky=tk.N+tk.S)

		# Create SignIn button
		style = ttk.Style()
		style.configure("RoundedButton.TButton", borderwidth=0, relief="flat", background="#c9c9c9", foreground="black", font=("Helvetica", 10))
		style.map("RoundedButton.TButton", background=[("active", "#a9a9a9")])

		self.__signInButton = ttk.Button(self, text="Sign In", command=self.__signIn, style="RoundedButton.TButton")
		self.__signInButton.grid(row=3, column=1, padx=10, pady=10, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S)

		# Create SignUp button
		self.__signUpButton = ttk.Button(self, text="Sign Up", command=lambda: self.__controller.showFrame("SignUp"), style="RoundedButton.TButton")
		self.__signUpButton.grid(row=4, column=1, padx=10, pady=5, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S)

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
		if (self.__controller.validate(identity, password)):
			self.__identity.delete(0, tk.END)
			self.__password.delete(0, tk.END)
			self.__controller.showFrame("Home")
		else:
			messagebox.showerror("Error", "Incorrect username or password")
			return