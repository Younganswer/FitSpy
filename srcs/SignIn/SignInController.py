class SignInController:
	def __init__(self, window):
		pass

	@classmethod
	def validate(self, identity, password):
		return (identity == "admin" and password == "password")