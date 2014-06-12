import math

class Circle(object):

	version = '1.0'
	
	def __init__(self, radius):
		self.radius=radius
		
	
	def area(self):
		return math.pi * self.radius ** 2
		
		
print 'ciruituous'
c=Circle(10)
print 'a circle of radious', c.radius
print 'has an area of', c.area()