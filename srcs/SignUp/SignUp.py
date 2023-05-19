import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class SignUp(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.__controller = controller
		self.__createWidgets()
	
	def __del__(self):
		pass