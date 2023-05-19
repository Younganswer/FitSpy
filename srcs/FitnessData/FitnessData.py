class FitnessData:
    def __init__(self, amountOfUsedCalories=0, timeOfWorkedOut=0):
        self.__amountOfUsedCalories = amountOfUsedCalories
        self.__timeOfWorkedOut = timeOfWorkedOut

    def getAmountOfUsedCalories(self):
        return (self.__amountOfUsedCalories)

    def getTimeOfWorkedOut(self):
        return (self.__timeOfWorkedOut)

    def setAmountOfUsedCalories(self, amountOfUsedCalories):
        self.__amountOfUsedCalories = amountOfUsedCalories

    def setTimeOfWorkedOut(self, timeOfWorkedOut):
        self.__timeOfWorkedOut = timeOfWorkedOut
