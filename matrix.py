#coding: utf-8

def transpose(matrix):
	ret = [[x for x in range(len(matrix))] for y in range(len(matrix[0]))]
	for y, row in enumerate(matrix):
		for x, cell in enumerate(row):
			ret[x][y] = cell
	return ret


class MatrixException(Exception):
	pass


class Matrix:

	def __init__(self, m, n):
		self.m = m
		self.n = n
		self.rows = [[0] * n for x in range(m)]


	def __str__(self):
		return "\n".join(map(str, self.rows))


	def __add__(self, other):
		if self.get_size() != other.get_size():
			raise MatrixException("Both matrixes should be of the same size.")
		ret = Matrix(self.m, self.n)
		for index, row in enumerate(self.rows):
			ret[index] = [a + b for a, b in zip(row, other[index])]
		return ret


	def __sub__(self, other):
		if self.get_size() != other.get_size():
			raise MatrixException("Both matrixes should be of the same size.")
		ret = Matrix(self.m, self.n)
		for index, row in enumerate(self.rows):
			ret[index] = [a - b for a, b in zip(row, other[index])]
		return ret


	def __mul__(self, other):
		if isinstance(other, (int, float)):
			return [[elem * other for elem in row] for row in self.rows]
		elif isinstance(other, (Matrix, list)):
			m2, n2 = other.get_size() if isinstance(other, Matrix) else (len(other), 1)
			# if (isinstance(other, list)) or (n2 == 1 and m2 == self.n) or (self.n == 1 and self.n == m2):
			# 	ret = Matrix(self.m, 1)
			# 	for index, row in enumerate(self.rows):
			# 		ret[index] = row * other[index]
			# else:
			if self.n == m2 or n2 == self.m:
				ret = Matrix(self.m, self.n)
				for x in range(self.m):
					for y in range(other.m if isinstance(other, Matrix) else len(other)):
						print(self.rows[x], other[y])
						ret[x][y] = sum([a * b for a, b in zip(self.rows[x], other)])
			else:
				raise MatrixException("Matrixes' sizes do not correspond.")
			return ret
		else:
			raise MatrixException("TypeError: expected Matrix, int or float type")


	def __getitem__(self, index):
		return self.rows[index]


	def __setitem__(self, index, value):
		if isinstance(value, list):
			if len(value) != self.n:
				raise MatrixException("ValueError: value does not have the same width as matrix{}".format(self.get_size()))
			elif not all([isinstance(item, (int, float)) for item in value]):
				raise MatrixException("TypeError: Only int and float should be in the list.")
			self.rows[index] = value


	def get_size(self):
		return (self.m, self.n)

	def transpose(self):
		self.m, self.n = self.n, self.m
		self.rows = [list(row) for row in zip(*self.rows)]
