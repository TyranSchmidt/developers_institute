class Currency():
	def __init__(self, amount=0.00, label="Shekels"):
		self.amount = amount
		self.label = label
	def __str__(self):
		return str(self.amount)
	def __repr__(self):
		return (f"The total amount is {self.amount} {self.label}.")
	def __int__(self):
		return int(self.amount)
	def add_amount(self, amount):
		self.amount += amount
	def add_other_currency(self, second):
		if self.label == second.label:
			self.amount += second.amount
		else:
			raise Exception("The currency types don't match.")
	def subtract_amount_by_5(self, amount):
		self.amount -= 5
	def subtract_other_currency(self, second):
		if self.label == second.label:
			self.amount -= second.amount
		else:
			raise Exception("The currency types don't match.")
	def multiply_amount_by_5(self, amount):
		self.amount *= 5
	def multiply_other_currency(self, second):
		if self.label == second.label:
			self.amount *= second.amount
		else:
			raise Exception("The currency types don't match.")
	def divide_amount_by_5(self, amount):
		self.amount /= 5
	def divide_other_currency(self, second):
		if self.label == second.label:
			self.amount /= second.amount
		else:
			raise Exception("The currency types don't match.")	
	def print_methods(self):
		print(dir(Currency))				


class Circle():
	def __init__(self, radius=0, diameter=0):
		self.radius = radius
		self.diameter = diameter
		if radius != 0:
			self.area = math.pi * (self.radius**2)
		elif diameter != 0:
			self.area = math.pi * ((self.diameter/2)**2)
	def get_dia(self):
		print(self.diameter)
	def get_radius(self):
		print(self.radius)
	def get_area(self):
		print(self.area)
	def print_circle(self):
		print("O")
	def add_two_circles(self, circle2):
		self.area += circle2.area
		print(f"The total area of the circle is now {self.area}") 
	def bigger_circle(self, circle2):
		if self.area > circle2.area:
			print("This circle is bigger")
		elif circle2.area > self.area:
			print(f"{circle2} is bigger")
		else:
			print("They are the same size")	
	def equal_circles(self, circle2):
		if self.area == circle2.area:
			print("They are equal size")
		else:
			print("They are not equal size")


cir_list = []
cir_list.append(cir1)
cir_list.append(cir2)
cir_list.sort()

		
		

