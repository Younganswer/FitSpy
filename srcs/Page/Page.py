from abc import ABC, abstractmethod
import tkinter as tk

class APage(ABC, tk.Frame):
	def	__init__(self, parent, controller):
		ABC.__init__(self)
		tk.Frame.__init__(self, parent)
		self._controller = controller
		self._set_widgets()

	def	__del__(self):
		pass

	@abstractmethod
	def	_set_page(self):
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
		from SignIn.SignIn import SignIn
		from SignUp.SignUp import SignUp
		from Home.TraineeHome import TraineeHome
		from Home.TrainerHome import TrainerHome

		if page_name == "SignIn":
			return SignIn(parent, controller)
		elif page_name == "SignUp":
			return SignUp(parent, controller)
		elif page_name == "TraineeHome":
			return TraineeHome(parent, controller)
		elif page_name == "TrainerHome":
			return TrainerHome(parent, controller)
		else:
			raise ValueError("PageFactory: Invalid page name")