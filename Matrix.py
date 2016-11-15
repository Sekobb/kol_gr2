class Matrix(object):
	def __init__(self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d				

	def __str__(self):
		return str(self.a) + ", " + str(self.b) + ", " + str(self.c) + ", " + str(self.d)

	def __add__(self, oth):
		if isinstance(oth, Matrix):
			new_a = self.a + oth.a
			new_b = self.b + oth.b
			new_c = self.c + oth.c
			new_d = self.d + oth.d
			return Matrix(new_a, new_b, new_c, new_d)
		elif isinstance(oth, (int, long, float)):
			new_a = self.a + oth
			new_b = self.b + oth
			new_c = self.c + oth
			new_d = self.d + oth
			return Matrix(new_a, new_b, new_c, new_d)
		else:
			return Matrix(0, 0, 0, 0)

	def __radd__(self, oth):
		return self.__add__(oth)

	def __sub__(self, oth):
		if isinstance(oth, Matrix):
			new_a = self.a - oth.a
			new_b = self.b - oth.b
			new_c = self.c - oth.c
			new_d = self.d - oth.d
			return Matrix(new_a, new_b, new_c, new_d)
		elif isinstance(oth, (int, long, float)):
			new_a = self.a - oth
			new_b = self.b - oth
			new_c = self.c - oth
			new_d = self.d - oth
			return Matrix(new_a, new_b, new_c, new_d)
		else:
			return Matrix(0, 0, 0, 0)

	def __mul__(self, oth):
		if isinstance(oth, Matrix):
			new_a = (self.a*oth.a) + (self.b*oth.c)
			new_b = (self.a*oth.b) + (self.b*oth.d)
			new_c = (self.c*oth.a) + (self.d*oth.b)
			new_d = (self.c*oth.b) + (self.d*oth.d)
			return Matrix(new_a, new_b, new_c, new_d)
		elif isinstance(oth, (int, long, float)):
			new_a = self.a * oth
			new_b = self.b * oth
			new_c = self.c * oth
			new_d = self.d * oth
			return Matrix(new_a, new_b, new_c, new_d)
		else:
			return Matrix(0, 0, 0, 0)

	def __rmul__(self, oth):
		return self.__mul__(oth)

	def summ(self, oth):
		return self.__add__(oth)

	def diff(self, oth):
		return self.__sub__(oth)

	def mult(self, oth):
		return self.__mul__(oth)

	def vector(self):
		i = 0
		v = [self.a, self.b]
		while i < 2:
			yield v
			v = [self.c, self.d]
			i = i + 1

		
