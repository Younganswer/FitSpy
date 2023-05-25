import os
import sys

from PageController.PageController import PageController


def initDB():
    db = []
    """
	user1 = UserData(PersonalInformaion(identity, password, name, phoneNumber, sex, email, accountType))
	user2 = UserData(PersonalInformaion(identity, password, name, phoneNumber, sex, email, accountType))
	user3 = UserData(PersonalInformaion(identity, password, name, phoneNumber, sex, email, accountType))
	db.append(user1)
	db.append(user2)
	db.append(user3)
	"""
    return db


"""
TODO: DB 만들어야되구요 - 조현준
TODO: DB는 다른 객체와의 연관성을 고민하면서 만들어야한다.
TODO: Trainee, Trainer Home page 만들어야되구요
TODO: Matching Page 만들어야되구요
TODO: advancedRecommendationAIModel() 에서 return(random % numberOfTrainer) - 조현준
TODO: AI도 하나의 객체(시스템)로 만들어야한다.
"""


def main():
    # db = initDB()
    window = PageController()
    window.mainloop()
    return 0


if __name__ == "__main__":
    os.environ["TK_SILENCE_DEPRECATION"] = "1"
    sys.path.append("srcs")
    main()
