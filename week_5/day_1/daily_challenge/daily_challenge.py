class X(): 
	def __init__(self, list, empty_list):
		self.start = list
		self.full = empty_list
	def subsets(self):
		self.full.append([])
		for a in self.start:
			self.full.append([a])
			for b in self.start:
				if b != a:
					if [a, b] in self.full or [b, a] in self.full:
						continue
					else:	
						self.full.append([a, b])
		self.full.append(self.start)							
		print(self.full)			
y = X([4, 5, 6], [])
		
y.subsets()		

class B():
	def __init__(self, list, empty_list):
		self.start2 = list
		self.full2 = empty_list
	def sum_zero(self):
		for a in self.start2:
			for b in self.start2:
				if b == a:
					continue
				for c in self.start2:
					if c == b or c == a:
						continue
					if a + b + c == 0:
						if [a, b, c] in self.full2 or [a, c, b] in self.full2 or [b, a, c] in self.full2 or [b, c, a] in self.full2 or [c, a, b] in self.full2 or [c, b, a] in self.full2:
							continue
						else:		
							self.full2.append([a, b, c])
		print(self.full2)					

c = B([-25, -10, -7, -3, 2, 4, 8, 10], [])

c.sum_zero()

