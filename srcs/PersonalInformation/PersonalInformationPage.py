import tkinter as tk
from tkinter import ttk
from Page.Page import APage

class PersonalInformationPage(APage):
	def __init__(self, parent, controller):
		super().__init__(parent, controller)
		self._set_widgets()

	def __del__(self):
		pass

	def	_set_widgets(self):
		self.__set_title()
		self.__set_labels()

	def __set_title(self):
		self.__title = ttk.Label(self, text="Personal Information", font=("Helvetica", 20))
		self.__title.place(x=180, y=180, anchor="center")

	def __set_labels(self):
		pass