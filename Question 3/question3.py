class Cylinder:
	def __init__(self,radius,height):
		self.radius=radius
		self.height=height

	def Surface_area_of_a_cylinder(self):
		radius=self.radius
		height=self.height
		Surface_area_of_a_cylinder=2*3.142*radius*radius+2*3.142*radius*height
		
		return(Surface_area_of_a_cylinder)

	def Volume_of_a_cylinder(self):
		radius=self.radius
		height=self.height
		Volume_of_a_cylinder=3.142*radius*radius*height
		
		return(Volume_of_a_cylinder)
