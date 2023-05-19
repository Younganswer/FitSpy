import os
import sys

import tkinter as tk

from PageController.PageController import PageController
from SignIn.SignIn import SignIn
from SignUp.SignUp import SignUp
from Home.Home import Home

def	keyPressed(window, event):
	if event.keysym == 'Escape':
		window.destroy()

def initWindow():
	window = tk.Tk()
	window.title("Fitspy")
	window.geometry("360x640")
	window.resizable(False, False)
	window.bind('<Key>', lambda event: keyPressed(window, event))
	return (window)

def	initPageController(window):
	pageController = PageController()
	pageController.addFrame(SignIn(window, pageController))
	pageController.addFrame(SignUp(window, pageController))
	pageController.addFrame(Home(window, pageController))
	return (pageController)

def main():
	window = initWindow()
	pageController = initPageController(window)
	pageController.showFrame("SignIn")
	window.mainloop()
	return (0)

if __name__ == "__main__":
	os.environ['TK_SILENCE_DEPRECATION'] = '1'
	sys.path.append("srcs")
	main()