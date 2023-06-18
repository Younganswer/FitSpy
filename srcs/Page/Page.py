from abc import ABC, abstractmethod
import tkinter as tk

# Polymorphism
# Abstract class
# Declare pure virtual functions to force subclasses to implement them
class APage(ABC, tk.Frame):
	def	__init__(self, parent, controller):
		ABC.__init__(self)
		tk.Frame.__init__(self, parent)
		self._controller = controller

	def	__del__(self):
		pass

	@abstractmethod
	def	_set_widgets(self):
		pass

# Factory pattern
# Pure fabrication
# Singleton pattern
class PageFactory:
	__instance = None

	def	__new__(cls):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
		return cls.__instance
	
	def	create_page(self, page_name, parent, controller):
		from SignIn.SignInPage import SignInPage
		from SignUp.SignUpPage import SignUpPage
		from Trainee.TraineePage import TraineePage
		from Trainer.TrainerPage import TrainerPage
		from PersonalInformation.PersonalInformationPage import PersonalInformationPage
		from Matching.MatchingPage import MatchingPage

		pages = {
			"SignIn": SignInPage,
			"SignUp": SignUpPage,
			"Trainee": TraineePage,
			"Trainer": TrainerPage,
			"PersonalInformation": PersonalInformationPage,
			"Matching": MatchingPage
		}

		if page_name not in pages:
			raise ValueError("PageFactory: Invalid page name")

		return pages[page_name](parent, controller)