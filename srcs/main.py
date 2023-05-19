import os
import sys

import tkinter as tk

from SignIn.SignIn import SignIn
from SignIn.SignInController import SignInController

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

def main():
	window = initWindow()
	signIn = SignIn(window, SignInController(window))
	window.mainloop()
	return (0)

if __name__ == "__main__":
	os.environ['TK_SILENCE_DEPRECATION'] = '1'
	sys.path.append("srcs")
	main()