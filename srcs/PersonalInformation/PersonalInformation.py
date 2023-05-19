class PersonalInformation:
    def __init__(self, identity, password, name, phoneNumber, sex, email, accountType):
        self.__identity = identity
        self.__password = password
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__sex = sex
        self.__email = email
        self.__accountType = accountType

    def getName(self):
        return (self.__name)

    def getPhoneNumber(self):
        return (self.__phoneNumber)

    def getSex(self):
        return (self.__sex)

    def getEmail(self):
        return (self.__email)

    def getAccountType(self):
        return (self.__accountType)

    def getIdentity(self):
        return (self.__identity)

    def getPassword(self):
        return (self.__password)

    def setEmail(self, email):
        self.__email = email

    def setPassword(self, password):
        self.__password = password
