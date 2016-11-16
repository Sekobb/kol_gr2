import math

class Matrix(object):
	def __init__(self, *values):
		self.m = []
		for el in values:
			self.m.append(el)				

	def __str__(self):
		res = ""
		for i in range(len(self.m)-1):
			res += str(self.m[i]) + ", "
		res += str(self.m[len(self.m)-1])
		return res

	def __add__(self, oth):
		if isinstance(oth, Matrix):
			new = Matrix()
			for i in range(len(self.m)):
				new.m.append(self.m[i] + oth.m[i])
			return new
		elif isinstance(oth, (int, long, float)):
			new = Matrix()
			for i in range(len(self.m)):
				new.m.append(self.m[i] + oth)
			return new
		else:
			return Matrix()

	def __radd__(self, oth):
		return self.__add__(oth)

	def __sub__(self, oth):
		if isinstance(oth, Matrix):
			new = Matrix()
			for i in range(len(self.m)):
				new.m.append(self.m[i] - oth.m[i])
			return new
		elif isinstance(oth, (int, long, float)):
			new = Matrix()
			for i in range(len(self.m)):
				new.m.append(self.m[i] - oth)
			return new
		else:
			return Matrix()

	def __mul__(self, oth):
		if isinstance(oth, Matrix):
			new = Matrix()
			for i in range((int)(math.sqrt(len(self.m)))):
				for j in range((int)(math.sqrt(len(self.m)))):
					sum = 0
					for k in range((int)(math.sqrt(len(self.m)))):
						sum += self.m[i*(int)(math.sqrt(len(self.m))) + k]*oth.m[k*(int)(math.sqrt(len(self.m))) + j]
					new.m.append(sum)
			return new
		elif isinstance(oth, (int, long, float)):
			new = Matrix()
			for i in range(len(self.m)):
				new.m.append(self.m[i] * oth)
			return new
		else:
			return Matrix()

	def __rmul__(self, oth):
		return self.__mul__(oth)

	def summ(self, oth):
		return self.__add__(oth)

	def diff(self, oth):
		return self.__sub__(oth)

	def mult(self, oth):
		return self.__mul__(oth)

	def vector(self):
		tmp = 0
		v = []
		for el in self.m:
			v.append(el)
			if tmp%math.sqrt(len(self.m)):
				yield v
				v = []
			tmp += 1
		

		
