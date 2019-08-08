class person:

	def __init__(self):
		self.name = ''
		self.age = ''
		self.scope = ''

	def __str__(self):
		# num = self.age + self.scope
		return self.name + str(self.age) + str(self.scope)


def test_git():
	p = person()
	p.name = "zy"
	p.scope = 1
	p.age = 2
	print(p)


test_git()
