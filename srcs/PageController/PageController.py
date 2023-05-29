import tkinter as tk
from SignIn.SignIn import SignIn
from SignUp.SignUp import SignUp
from Home.TraineeHome import TraineeHome
from Home.TrainerHome import TrainerHome


class PageController(tk.Tk):
	def __init__(self):
		super().__init__()
		self.__set_window_configurations()
		self.__frames = self.__init_frames()
		self.__current_frame = None
		self.show_frame("SignIn")

	def __del__(self):
		pass
		
	def __set_window_configurations(self):
		self.title("Fitspy")
		self.geometry("360x640")
		self.resizable(False, False)
		self.bind("<Key>", lambda event: self.__key_pressed(event))

	def __key_pressed(self, event):
		if event.keysym == "Escape":
			self.destroy()

	def __init_frames(self):
		frames = {}
		for frame in (SignIn, SignUp, TraineeHome, TrainerHome):
			frames[frame.__name__] = frame(parent=self, controller=self)
		return frames

	def show_frame(self, page_name):
		if page_name not in self.__frames:
			raise ValueError("Invalid page name")
		if self.__current_frame is not None:
			self.__current_frame.pack_forget()
		self.__current_frame = self.__frames[page_name]
		self.__current_frame.pack(fill="both", expand=True)