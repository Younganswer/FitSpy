from DB.DB import DB


class SignInController:
	def __init__(self):
		pass

	@staticmethod
	def	get_user_data(identity, password):
		user_data = DB.get_user_data()
		for user in user_data:
			print("user.get_identity() = {}, user.get_password() = {}".format(user.get_identity(), user.get_password()))
			if user.get_identity() == identity and user.get_password() == password:
				return user
		return None