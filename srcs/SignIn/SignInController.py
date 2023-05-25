from DB.DB import DB


class SignInController:
	def __init__(self):
		pass

	@staticmethod
	def	get_user_data(self, identity, password):
		user_data = DB.get_user_data()
		for user in user_data:
			if user.get_identity() == identity and user.get_password() == password:
				return user
		return None