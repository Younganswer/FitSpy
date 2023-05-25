class UserData:
	def __init__(self, personalInformation):
		self.__personalInformation = personalInformation
		self.__progress = []

	def __del__(self):
		pass

	def getPersonalInformation(self):
		return self.personalInformation

	def getProgress(self):
		return self.progress

	def appendProgress(self, progress):
		self.__progress.append(progress)
