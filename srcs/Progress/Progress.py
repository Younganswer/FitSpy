class Progress:
	def __init__(self, fitnessData, feedback, diet):
		self.__fitnessData = fitnessData
		self.__feedback = feedback
		self.__diet = diet
	
	def __del__(self):
		pass

	def getFitnessData(self):
		return (self.__fitnessData)

	def getFeedback(self):
		return (self.__feedback)

	def getDiet(self):
		return (self.__diet)