class InputError(Exception):
	def __init__(self,message,errors):
		self.message = message

		super(InputError,self).__init__(message)
		self.errors = errors