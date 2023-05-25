class FitnessData:
	def __init__(self, amount_of_used_calories=0, time_of_worked_out=0):
		self.__amount_of_used_calories = amount_of_used_calories
		self.__time_of_worked_out = time_of_worked_out

	def get_amount_of_used_calories(self):
		return (self.__amount_of_used_calories)

	def get_time_of_worked_out(self):
		return (self.__time_of_worked_out)

	def set_amount_of_used_calories(self, amount_of_used_calories):
		self.__amount_of_used_calories = amount_of_used_calories

	def set_time_of_worked_out(self, time_of_worked_out):
		self.__time_of_worked_out = time_of_worked_out
