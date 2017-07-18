class Foo(object):
	def __init__(self, func):
		self.func = func

	def __call__(self):
		print 'Yes';
		self.func()
		print ('finish')

@Foo
def bar():
	print 'bar'

bar()