import tkinter as tk
from tkinter import ttk

class TraineeHome(tk.Frame):
	def __init__(self, parent, controller):
		super().__init__(parent)
		self.__controller = controller
		self.__my_trainees = {}
		self.__set_widgets()
	
	def __del__(self):
		pass

	def __set_widgets(self):
		self.__set_title()
		self.__set_buttons()
		self.__set_labels()

	def __set_title(self):
		self.__title = ttk.Label(self, text="My trainees", font=("Helvetica", 20), anchor="center")
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
		self.__personal_information_button = ttk.Button(self, image=self.__personal_information_image, style="RoundedButton.TButton", command=lambda: self.__controller.show_frame("PersonalInformation"))
		self.__personal_information_button.place(x=330, y=30, width=40, height=40, anchor="center")

		i = 0
		for traniee in self.__my_trainees:
			check_progress_button = ttk.Button(self, text="Check progress", style="RoundedButton.TButton", command=lambda: self.__controller.show_frame("CheckProgress"))
			check_progress_button.place(x=250, y=300+i*40, width=130, height=30, anchor="center")
			i += 1
	
	def	__set_labels(self):
		i = 0
		for trainee in self.__my_trainees:
			trainee_name_label = ttk.Label(self, text=trainee.get_name(), font=("Helvetica", 10), anchor="center")
			trainee_name_label.place(x=110, y=300+i*40, width=130, height=30, anchor="center")
			i += 1