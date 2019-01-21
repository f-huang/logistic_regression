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


def accuracy(my_y, his_y):
	diff = his_y - my_y
	return 1 - (np.count_non_zero(diff)) / len(diff)


def decision_boundary(probability):
	return 1 if probability > 0.5 else 0


def sigmoid(z):
	'''
	z: (m, 1)

	Sigmoid = 1 / 1e(-z)
	'''
	return np.array([1 / (1 + math.exp(-x)) for x in z])


def predict(features, weights):
	return sigmoid(np.dot(features, weights))


def cost_function(X, y, weights):
	'''
	Using Cross-Entropy / Log Cross

	X: (m, 1)
	y: (m, 1)
	weights: (n, 1)
	Returns 1D matrix of predictions

	Cost = (y * log(predictions) + (1-y)*log(1-predictions)) / len(X)
	'''

	predictions = predict(X, weights)
	cost_1 = -y * np.log(predictions)
	cost_2 = (1 - y) * np.log(1 - predictions)
	return (cost_1 - cost_2).sum() / len(X)


def update_weights(X, y, weights):
	'''
	X: (m, 1)
	y: (m, 1)
	weights: (n, 1)
	'''
	learning_rate = 12

	predictions = predict(X, weights)
	gradient = np.dot(X.T, predictions - y)
	return weights - gradient / len(X) * learning_rate


def train(X, y, current_train):
	cost_history = []
	weights = np.array([0.0] * len(X.columns))
	yh = np.where(y == current_train, 1.0, 0.0)
	for _ in range(1000):
		weights = update_weights(X, yh, weights)
		cost = cost_function(X, yh, weights)
		cost_history.append(cost)
	return {'weights': weights, 'cost_history': cost_history}


def one_vs_all(df, label, features, all):
	X = df.loc[:, features]
	y = df[label]
	ret = {key: None for key in all}
	for one in all:
		ret[one] = train(X, y, one)


if __name__ == "__main__":

	features = [
		# 'Astronomy',
		# 'Herbology',
		# 'Defense Against the Dark Arts',
		# 'Divination',
		'Muggle Studies',
		# 'Ancient Runes',
		# 'History of Magic',
		# 'Transfiguration',
		# 'Potions',
		'Charms',
		'Flying'
	]

	file = "res/dataset_train.csv"
	dataset = read_file(file, ignore=True)
	df = normalize_df(pd.DataFrame(dataset[1:], columns=dataset[0]))
	one_vs_all(df, 'Hogwarts House', features, get_houses())
