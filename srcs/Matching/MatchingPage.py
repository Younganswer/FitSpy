import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Page.Page import APage
from Matching.MatchingSystem import TheMostAdvancedAIWithTheLatestTechnology

class MatchingPage(APage):
	def __init__(self, parent, controller):
		super().__init__(parent, controller)
		self._set_widgets()

	def __del__(self):
		pass

	def	_set_widgets(self):
		self.__set_title()
		self.__set_buttons()

	def __set_title(self):
		self.__title = ttk.Label(self, text="Matching Trainer", font=("Helvetica", 20))
		self.__title.place(x=180, y=200, anchor="center")

	def __set_buttons(self):
		style = ttk.Style()
		style.configure(
			"RoundedButton.TButton",
			borderwidth=0,
			relief="flat",
			background="#c9c9c9",
			foreground="black",
			font=("Helvetica", 10),
		)
		style.map("RoundedButton.TButton", background=[("active", "#a9a9a9")])

		self.__matching_button = ttk.Button(
			self,
			text="Matching",
			command=self.__matching,
			style="RoundedButton.TButton",
		)
		self.__matching_button.place(x=180, y=400, width=270, height=25, anchor="center")

	def __matching(self):
		try:
			trainer = TheMostAdvancedAIWithTheLatestTechnology.matching_trainer()
			messagebox.showinfo("Success", "Your trainer is " + trainer.get_name())
		except Exception as e:
			messagebox.showerror("Error", str(e))