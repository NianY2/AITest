import utils.glo as glo
class Test:
	id = 0
	def __init__(self,id):
		self.id = id
		glo.set_value('is_login',self.is_login)
	def is_login(self):
		print('id',self.id)
		return self.id == 1