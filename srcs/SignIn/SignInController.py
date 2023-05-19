class SignInController:
	def __init__(self, window):
		pass

	def validate(self, identity, password):
		return (identity == "admin" and password == "password")

	def showFrame(self, className):
		print("Sign Up button clicked")