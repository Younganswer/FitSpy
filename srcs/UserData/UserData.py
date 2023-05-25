class UserData:
    def __init__(self, personalInformation):
        self.__personalInformation = personalInformation
        self.__progress = []

    def __del__(self):
        pass

    def getPersonalInformation(self):
        return self.__personalInformation

    def getProgress(self):
        return self.__progress

    def appendProgress(self, progress):
        self.__progress.append(progress)

    def getIDPW(self):
        return [
            self.__personalInformation.getId(),
            self.__personalInformation.getPassword(),
        ]

    def getAccountType(self):
        return self.__personalInformation.getAccountType()
