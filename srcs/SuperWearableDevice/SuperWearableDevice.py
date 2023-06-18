from FitnessData.FitnessData import FitnessData

class SuperWearableDevice:
	__instance = None

	def	__new__(cls):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
		return cls.__instance

	def	get_fitness_data(self):
		return FitnessData(100, 60)

	def	get_diet(self):
		return 2100