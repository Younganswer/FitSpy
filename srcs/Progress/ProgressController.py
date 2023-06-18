from Progress.Progress import Progress
from UserData.UserDataController import UserDataController

class ProgressController:
	__instance = None

	def	__new__(cls):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
		return cls.__instance

	def	get_progress(self):
		controller = UserDataController()
		user_data = controller.get_user_data()
		return user_data.get_progress()

	def	set_progress(self, progress):
		controller = UserDataController()
		user_data = controller.get_user_data()
		user_data.set_progress(progress)