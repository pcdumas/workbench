import math

class Circle(object):

	version = '1.0'
	
	def __init__(self, radius):
		self.radius=radius
		
	
	def area(self):
		return math.pi * self.radius ** 2
		