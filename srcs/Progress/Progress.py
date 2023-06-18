class Progress:
	def __init__(self, fitness_data, diet, feedback):
		self.__fitness_data = fitness_data
		self.__diet = diet
		self.__feedback = feedback
	
	def __del__(self):
		pass

	def get_fitness_data(self):
		return (self.__fitness_data)

	def get_diet(self):
		return (self.__diet)

	def get_feedback(self):
		return (self.__feedback)