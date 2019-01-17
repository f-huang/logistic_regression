#!/usr/bin/env python3
# coding: utf-8

import sys
import math
import numpy as np
import pandas as pd
from hp_tools import get_houses, get_disciplines
from tools import read_file

## J(θ) = − (1/m) sum( yi log(hθ(xi)) + (1 − yi) log(1 − hθ(xi)))
## hθ(x) = g(θT x)
## g(z) = 1 / 1+e−z
## ∂ / ∂θj J(θ) =  1/m sum(hθ(xi) − yi)xij m i=1


def sigmoid(z):
	return 1 / (1 + math.exp(-z))


def get_hypothesis_function(thetas):
	def f(x):
		return sigmoid(np.dot(thetas, x))
	return f


def derivative(df, house, discipline, h):
	return float(sum([
			(h([student[discipline] for discipline in get_disciplines()])\
			- int(student['Hogwarts House'] == house)) * student[discipline]
			for index, student in df.iterrows()
		])) / len(df)


def train(df):
	discplines = get_disciplines()
	thetas, learning_rate = dict.fromkeys(discplines, 0.0), 1.5
	i, cost = 0, 100
	while i < 1000:
		for house in get_houses():
			for index, student in df.iterrows():
				h = get_hypothesis_function(list(thetas.values()))
				for discipline in discplines:
					thetas[discipline] -= learning_rate\
					* derivative(df, house, discipline, h)
		old_cost = cost
		if abs(old_cost - cost) < 10e-11:
			break
		i += 1
	return thetas


if __name__ == "__main__":
	file = "res/dataset_train.csv"
	dataset = read_file(file)
	df = pd.DataFrame(dataset[1:], columns=dataset[0])
	# print(len(df))
	train(df)
