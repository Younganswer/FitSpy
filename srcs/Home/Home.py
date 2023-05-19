import tkinter as tk
from tkinter import ttk

class Home(tk.Frame):
	def __init__(self, parent, controller):
		super().__init__(parent)
		self.__controller = controller
		self.__setWidgets()
		self.__show()
	
	def __del__(self):
		pass

	def __setWidgets(self):
		pass

	def __show(self):
		self.pack(fill=tk.BOTH, expand=True)