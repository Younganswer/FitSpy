import pickle
import os
import sys

# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
os.chdir("..")
print("pwd :", os.getcwd())


class DB:
    __db = []

    def __init__(self):
        with open("./UserDB/accounts.pickle", "rb") as fr:
            DB.__db = pickle.load(fr)
            fr.close()

    def get_DB(self):
        return DB.__db

    def SignUp(self, userData):
        DB.__db.append(userData)
        with open("./UserDB/accounts.pickle", "wb") as fw:
            pickle.dump(DB.__db, fw)
            fw.close()
