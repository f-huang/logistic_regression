#!/usr/bin/env python3
# coding: utf-8

import sys
import math
import numpy as np
import pandas as pd
from hp_tools import get_houses, get_disciplines
from tools import read_file, normalize_df

## J(θ) = − (1/m) sum( yi log(hθ(xi)) + (1 − yi) log(1 − hθ(xi)))
## hθ(x) = g(θT x)
## g(z) = 1 / 1+e−z
## ∂ / ∂θj J(θ) =  1/m sum(hθ(xi) − yi)xij m i=1

DISCIPLINES = [
	# 'Astronomy',
	# 'Herbology',
	# 'Defense Against the Dark Arts',
	# 'Divination',
	# 'Muggle Studies',
	# 'Ancient Runes',
	# 'History of Magic',
	# 'Transfiguration',
	# 'Potions',
	'Charms',
	'Flying'
]

def sigmoid(z):
	return 1 / (1 + math.exp(-z))


def distance(df, g):
	return float(sum(g(student) for index, student in df.iterrows())) / len(df)


def get_hypothesis_function(thetas):
	thetas = np.array(thetas).reshape((1, len(thetas)))
	def f(X):
		X = np.array(X).reshape((len(X), 1))
		return sigmoid(np.amax(X @ thetas))
	return f


def derivative(df, house, discipline, h):
	return distance(df, lambda student:
		(h([student[discipline] for discipline in DISCIPLINES])\
		- int(student['Hogwarts House'] == house)) * student[discipline])


def cost_function(df, house, h):
	error = [0] * len(df)
	for index, student in df.iterrows():
		y = int(student['Hogwarts House'] == house)
		hx = h([student[discipline] for discipline in DISCIPLINES])
		error[index] = y * math.log(hx) + (1 - y) * math.log(1 - hx)
	return -float(sum(error)) / len(df)


def train(df):
	thetas, learning_rate = dict.fromkeys(DISCIPLINES, 0.0), 100
	i, cost = 0, dict.fromkeys(DISCIPLINES, 0.0)
	old_cost = cost
	while i < 10:
		h = get_hypothesis_function(list(thetas.values()))
		for house in get_houses():
			for discipline in DISCIPLINES:
				if old_cost != cost and abs(old_cost[discipline] - cost[discipline]) < 10e-8:
					continue
				thetas[discipline] -= learning_rate\
				* derivative(df, house, discipline, h)
		for discipline in DISCIPLINES:
			cost[discipline] = cost_function(df, house, h)
		print(thetas)
		i += 1
	return thetas


if __name__ == "__main__":
	file = "res/dataset_train.csv"
	dataset = read_file(file, ignore=True)
	df = normalize_df(pd.DataFrame(dataset[1:], columns=dataset[0]))
	thetas = train(df)
