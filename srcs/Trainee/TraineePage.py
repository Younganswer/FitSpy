import tkinter as tk
from tkinter import ttk
from Page.Page import APage
from Progress.Progress import Progress
from Progress.ProgressController import ProgressController
from SuperWearableDevice.SuperWearableDevice import SuperWearableDevice

class TraineePage(APage):
	def __init__(self, parent, controller):
		super().__init__(parent, controller)
	
	def __del__(self):
		pass

	def _set_widgets(self):
		self.__update_progress()
		self.__set_title()
		self.__set_buttons()
		self.__set_labels()

	def	__update_progress(self):
		super_wearable_device = SuperWearableDevice()
		controller = ProgressController()
		controller.set_progress(Progress(super_wearable_device.get_fitness_data(), super_wearable_device.get_diet(), "Good"))

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
		controller = ProgressController()
		progress = controller.get_progress()
		fitness_data = progress.get_fitness_data()
		feedback = progress.get_feedback()

		self.__used_calories_label = ttk.Label(self, text="Used Calories", font=("Helvetica", 10), anchor="center")
		self.__work_out_time_label = ttk.Label(self, text="Work Out Time", font=("Helvetica", 10), anchor="center")
		self.__calories_of_diet_label = ttk.Label(self, text="Calories of Diet", font=("Helvetica", 10), anchor="center")
		self.__feedback_label = ttk.Label(self, text="Feedback", font=("Helvetica", 10), anchor="center")
		self.__used_calories_value_label = ttk.Label(self, text=fitness_data.get_amount_of_used_calories(), font=("Helvetica", 10), anchor="center")
		self.__work_out_time_value_label = ttk.Label(self, text=fitness_data.get_time_of_worked_out(), font=("Helvetica", 10), anchor="center")
		self.__calories_of_diet_value_label = ttk.Label(self, text=progress.get_diet(), font=("Helvetica", 10), anchor="center")
		self.__feedback_value_label = ttk.Label(self, text=feedback, font=("Helvetica", 10), anchor="center")

		self.__used_calories_label.place(x=135, y=300, width=110, height=20, anchor="center")
		self.__work_out_time_label.place(x=135, y=330, width=110, height=20, anchor="center")
		self.__calories_of_diet_label.place(x=335, y=260, width=110, height=20, anchor="center")
		self.__feedback_label.place(x=135, y=390, width=110, height=20, anchor="center")
		self.__used_calories_value_label.place(x=255, y=300, width=100, height=20, anchor="center")
		self.__work_out_time_value_label.place(x=255, y=330, width=100, height=20, anchor="center")
		self.__calories_of_diet_value_label.place(x=355, y=260, width=100, height=20, anchor="center")
		self.__feedback_value_label.place(x=255, y=390, width=100, height=20, anchor="center")

