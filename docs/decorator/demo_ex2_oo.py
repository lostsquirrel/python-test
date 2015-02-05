
class Log:
	def __call__(self, method):
		def __method(*args):
			
			handler = args[0]
			print handler.arg
		return __method

class ClassName():
  	"""docstring for ClassName"""
  	def __init__(self, arg):
  		self.arg = arg
  		
  	@Log()
  	def xx(self):
  		print 'hahaha'

if __name__ == "__main__":
	xx = ClassName(123)
	xx.xx()