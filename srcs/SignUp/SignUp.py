import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class SignUp(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.__controller = controller
		self.__setWidgets()
			
	def __del__(self):
		pass

	def __setWidgets(self):
		self.__setTitle()
		self.__setLabels()
		self.__setEnties()
		self.__setButton()

	def __setTitle(self):
		pass

	def __setLabels(self):
		pass

	def __setEnties(self):
		pass

	def __setButton(self):
		pass

	def	__show(self):
		self.pack(fill=tk.BOTH, expand=True)