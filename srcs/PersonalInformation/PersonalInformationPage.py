import tkinter as tk
from tkinter import ttk
from Page.Page import APage
from UserData.UserDataController import UserDataController

class PersonalInformationPage(APage):
	def __init__(self, parent, controller):
		super().__init__(parent, controller)

	def __del__(self):
		pass

	def	_set_widgets(self):
		self.__set_title()
		self.__set_labels()
		self.__set_values()

	def __set_title(self):
		self.__title = ttk.Label(self, text="Personal Information", font=("Helvetica", 20))
		self.__title.place(x=180, y=180, anchor="center")

	def __set_labels(self):
		self.__identity_label = ttk.Label(self, text="ID")
		self.__name_label = ttk.Label(self, text="Name")
		self.__phone_number_label = ttk.Label(self, text="Phone Number")
		self.__sex_label = ttk.Label(self, text="Sex")
		self.__email_label = ttk.Label(self, text="Email")
		self.__account_type_label = ttk.Label(self, text="Account Type")

		self.__identity_label.place(x=90, y=250, width=100, height=20, anchor="center")
		self.__name_label.place(x=90, y=280, width=100, height=20, anchor="center")
		self.__phone_number_label.place(x=90, y=310, width=100, height=20, anchor="center")
		self.__sex_label.place(x=90, y=340, width=100, height=20, anchor="center")
		self.__email_label.place(x=90, y=370, width=100, height=20, anchor="center")
		self.__account_type_label.place(x=90, y=400, width=100, height=20, anchor="center")
	
	def __set_values(self):
		controller = UserDataController()
		user_data = controller.get_cur_user_data()
		personal_information = user_data.get_personal_information()
		
		self.__identity = ttk.Label(self, text=personal_information.get_identity())
		self.__name = ttk.Label(self, text=personal_information.get_name())
		self.__phone_number = ttk.Label(self, text=personal_information.get_phone_number())
		self.__sex = ttk.Label(self, text=personal_information.get_sex())
		self.__email = ttk.Label(self, text=personal_information.get_email())
		self.__account_type = ttk.Label(self, text=personal_information.get_account_type())

		self.__identity.place(x=225, y=250, width=170, height=20, anchor="center")
		self.__name.place(x=225, y=280, width=170, height=20, anchor="center")
		self.__phone_number.place(x=225, y=310, width=170, height=20, anchor="center")
		self.__sex.place(x=225, y=340, width=170, height=20, anchor="center")
		self.__email.place(x=225, y=370, width=170, height=20, anchor="center")
		self.__account_type.place(x=225, y=400, width=170, height=20, anchor="center")
