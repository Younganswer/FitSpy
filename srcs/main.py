import os
import sys

from PageController.PageController import PageController
from DB.DB import DB

def main():
	window = PageController()
	window.mainloop()
	return 0


if __name__ == "__main__":
	os.environ["TK_SILENCE_DEPRECATION"] = "1"
	sys.path.append("srcs")
	main()
