import tkinter as tk
from tkinter import ttk
from Page.Page import APage

class TraineePage(APage):
	def __init__(self, parent, controller):
		super().__init__(parent, controller)
	
	def __del__(self):
		pass

	def _set_widgets(self):
		self.__set_title()
		self.__set_buttons()
		self.__set_labels()

	def __set_title(self):
		self.__title = ttk.Label(self, text="Today Progress", font=("Helvetica", 20), anchor="center")
		self.__title.place(x=180, y=160, anchor="center")

	def	__set_buttons(self):
		style = ttk.Style()
		style.configure(
			"RoundedButton.TButton",
			borderwidth=0,
			relief="flat",
			background="#c9c9c9",
			foreground="black",
		)
		style.map("RoundedButton.TButton", background=[("active", "#a9a9a9")])

		self.__personal_information_image = tk.PhotoImage(file="assets/PersonalInformationButton.png").subsample(16)
		self.__personal_information_button = ttk.Button(self, image=self.__personal_information_image, style="RoundedButton.TButton", command=lambda: self._controller.show_frame("PersonalInformation"))
		self.__personal_information_button.place(x=280, y=30, width=40, height=40, anchor="center")

		self.__find_trainer_image = tk.PhotoImage(file="assets/FindTrainerButton.png").subsample(16)
		self.__find_trainer_button = ttk.Button(self, image=self.__find_trainer_image, style="RoundedButton.TButton", command=lambda: self._controller.show_frame("Matching"))
		self.__find_trainer_button.place(x=330, y=30, width=40, height=40, anchor="center")
	
	def	__set_labels(self):
		# TODO: Get data from database
		self.__used_calories_label = ttk.Label(self, text="Used Calories", font=("Helvetica", 10), anchor="center")
		self.__work_out_time_label = ttk.Label(self, text="Work Out Time", font=("Helvetica", 10), anchor="center")
		self.__calories_of_diet_label = ttk.Label(self, text="Calories of Diet", font=("Helvetica", 10), anchor="center")
		self.__amount_of_used_calories_label = ttk.Label(self, text="250kcal", font=("Helvetica", 10), anchor="center")
		self.__time_of_work_out_label = ttk.Label(self, text="30min", font=("Helvetica", 10), anchor="center")
		self.__amount_of_calories_of_diet_label = ttk.Label(self, text="2000kcal", font=("Helvetica", 10), anchor="center")
		self.__used_calories_label.place(x=125, y=300, width=170, height=20, anchor="center")
		self.__work_out_time_label.place(x=125, y=340, width=170, height=20, anchor="center")
		self.__calories_of_diet_label.place(x=125, y=380, width=170, height=20, anchor="center")
		self.__amount_of_used_calories_label.place(x=260, y=300, width=100, height=20, anchor="center")
		self.__time_of_work_out_label.place(x=260, y=340, width=100, height=20, anchor="center")
		self.__amount_of_calories_of_diet_label.place(x=260, y=380, width=100, height=20, anchor="center")