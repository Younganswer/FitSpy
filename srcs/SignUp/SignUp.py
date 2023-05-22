import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class SignUp(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.__controller = controller
		self.__setWidgets()
		self.__show()
			
	def __del__(self):
		pass

	def __setWidgets(self):
		self.__setGridConfigure()
		self.__setTitle()
		self.__setLabels()
		self.__setEnties()
		self.__setButton()

	def __setGridConfigure(self):
		self.grid_rowconfigure(0, minsize=135)
		self.grid_rowconfigure(1, minsize=50)
		self.grid_rowconfigure(2, minsize=40)
		self.grid_rowconfigure(3, minsize=20)
		self.grid_rowconfigure(4, minsize=20)
		self.grid_rowconfigure(5, minsize=20)
		self.grid_rowconfigure(6, minsize=20)
		self.grid_rowconfigure(7, minsize=20)
		self.grid_rowconfigure(8, minsize=20)
		self.grid_rowconfigure(9, minsize=20)
		self.grid_rowconfigure(10, minsize=10)
		self.grid_rowconfigure(11, minsize=20)
		self.grid_rowconfigure(12, minsize=245)
		self.grid_columnconfigure(0, minsize=45)
		self.grid_columnconfigure(1, minsize=100)
		self.grid_columnconfigure(2, minsize=170)
		self.grid_columnconfigure(3, minsize=45)

	def __setTitle(self):
		self.__title = ttk.Label(self, text="Fitspy", font=("Helvetica", 30))
		self.__title.grid(row=1, column=1, columnspan=2)

	def __setLabels(self):
		self.__identityLabel = ttk.Label(self, text="ID")
		self.__passwordLabel = ttk.Label(self, text="Password")
		self.__nameLabel = ttk.Label(self, text="Name")
		self.__phoneNumberLabel = ttk.Label(self, text="Phone Number")
		self.__sexLabel = ttk.Label(self, text="Sex")
		self.__emailLabel = ttk.Label(self, text="Email")
		self.__accountTypeLabel = ttk.Label(self, text="Account Type")
		self.__identityLabel.grid(row=3, column=1, pady=5)
		self.__passwordLabel.grid(row=4, column=1, pady=5)
		self.__nameLabel.grid(row=5, column=1, pady=5)
		self.__phoneNumberLabel.grid(row=6, column=1, pady=5)
		self.__sexLabel.grid(row=7, column=1, pady=5)
		self.__emailLabel.grid(row=8, column=1, pady=5)
		self.__accountTypeLabel.grid(row=9, column=1, pady=5)

	def __setEnties(self):
		self.__identity = ttk.Entry(self, font=("Helvetica", 10))
		self.__password = ttk.Entry(self, font=("Helvetica", 10), show="*")
		self.__name = ttk.Entry(self, font=("Helvetica", 10))
		self.__phoneNumber = ttk.Entry(self, font=("Helvetica", 10))
		self.__sex = ttk.Combobox(self, font=("Helvetica", 10), state="readonly", textvariable=tk.StringVar(), values=['Male', 'Female'])
		self.__email = ttk.Entry(self, font=("Helvetica", 10))
		self.__accountType = ttk.Combobox(self, font=("Helvetica", 10), state="readonly", textvariable=tk.StringVar(), values=['Trainee', 'Trainer'])
		self.__identity.grid(row=3, column=2, pady=5, sticky=tk.W + tk.E)
		self.__password.grid(row=4, column=2, pady=5, sticky=tk.W + tk.E)
		self.__name.grid(row=5, column=2, pady=5, sticky=tk.W + tk.E)
		self.__phoneNumber.grid(row=6, column=2, pady=5, sticky=tk.W + tk.E)
		self.__sex.grid(row=7, column=2, pady=5, sticky=tk.W + tk.E)
		self.__email.grid(row=8, column=2, pady=5, sticky=tk.W + tk.E)
		self.__accountType.grid(row=9, column=2, pady=5, sticky=tk.W + tk.E)

	def __setButton(self):
		style = ttk.Style()
		style.configure("RoundedButton.TButton",
						borderwidth=0,
						relief="flat",
						background="#c9c9c9",
						foreground="black",
						font=("Helvetica", 10))
		style.map("RoundedButton.TButton", background=[("active", "#a9a9a9")])
		self.__signUpButton = ttk.Button(self, text="Sign Up", style="RoundedButton.TButton", command=self.__signUp)
		self.__signUpButton.grid(row=11, column=1, pady=5, columnspan=2, sticky=tk.W + tk.E)

	def	__show(self):
		self.pack(fill=tk.BOTH, expand=True)

	def	__signUp(self):
		identity = self.__identity.get()
		password = self.__password.get()
		name = self.__name.get()
		phoneNumber = self.__phoneNumber.get()
		sex = self.__sex.get()
		email = self.__email.get()
		accountType = self.__accountType.get()

		if (identity == "" or password == "" or name == "" or phoneNumber == "" or sex == "" or email == "" or accountType == ""):
			messagebox.showwarning("Warning", "Please fill in all the blanks.")
			return