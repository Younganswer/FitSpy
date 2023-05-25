class Progress:
	def __init__(self, fitness_data, feedback, diet):
		self.__fitness_data = fitness_data
		self.__feedback = feedback
		self.__diet = diet
	
	def __del__(self):
		pass

	def get_fitness_data(self):
		return (self.__fitness_data)

	def get_feedback(self):
		return (self.__feedback)

	def get_diet(self):
		return (self.__diet)