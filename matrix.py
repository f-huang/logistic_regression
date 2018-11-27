#coding: utf-8

def transpose(matrix):
	ret = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]
	for y, row in enumerate(matrix):
		for x, cell in enumerate(row):
			ret[x][y] = cell
	return ret
