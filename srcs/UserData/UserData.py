class UserData:
    def __init__(self, personalInformation, progress):
        self.personalInformation = personalInformation
        self.progress = progress

	def __del__(self):
		pass

	def getPersonalInformation(self):
		return (self.personalInformation)

	def getProgress(self):
		return (self.progress)