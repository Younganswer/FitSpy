import os
import sys

from PageController.PageController import PageController
from DB.DB import DB

def main():
	for user in DB.get_user_data():
		print(user.get_personal_information().get_name())
	window = PageController()
	window.mainloop()
	return 0


if __name__ == "__main__":
	os.environ["TK_SILENCE_DEPRECATION"] = "1"
	sys.path.append("srcs")
	main()
