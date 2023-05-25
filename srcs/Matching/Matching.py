import os
import sys
import random

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from UserDB.DB import DB


class Matching:
    def __init__(self):
        self.__db = DB().get_DB()
        self.__Trainers = [
            i.getPersonalInformation().getName()
            for i in self.__db
            if i.getAccountType() == "Trainer"
        ]

    def MatchingTrainer(self):
        return self.__Trainers[
            random.randint(0, len(self.__Trainers)) % len(self.__Trainers)
        ]
