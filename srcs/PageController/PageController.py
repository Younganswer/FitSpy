class PageController:
	def __init__(self):
		self.__frames = {}
		self.__currentPage = None

	def __del__(self):
		pass

	def	addFrame(self, frame):
		self.__frames[frame.__class__.__name__] = frame

	def	showFrame(self, className):
		if self.__currentPage != None:
			self.__currentPage.pack_forget()
		self.__frames[className].tkraise()
		self.__currentPage = self.__frames[className]