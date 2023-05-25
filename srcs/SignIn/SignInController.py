from UserDB.DB import DB


class SignInController:
    def __init__(self):
        self.db = DB().get_DB()
        self.accounts = dict([i.getIDPW() for i in self.db])
        self.IDs = [key for key in self.accounts]

    def validate(self, identity, password):
        if identity in self.IDs:
            return self.accounts[identity] == password
        return False
