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
