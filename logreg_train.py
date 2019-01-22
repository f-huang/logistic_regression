#!/usr/bin/env python3
# coding: utf-8

import sys
import math
import numpy as np
import pandas as pd
from hp_tools import get_houses, get_disciplines, get_features
from tools import read_file, normalize_df

## J(θ) = − (1/m) sum( yi log(hθ(xi)) + (1 − yi) log(1 − hθ(xi)))
## hθ(x) = g(θT x)
## g(z) = 1 / 1+e−z
## ∂ / ∂θj J(θ) =  1/m sum(hθ(xi) − yi)xij m i=1

def save_weights_into(path, weights):
	np.save(path, weights)


def accuracy(my_y, his_y):
	diff = his_y - my_y
	return 1 - (np.count_nonzero(diff)) / len(diff)


def decision_boundary(probability):
	return 1 if probability > 0.5 else 0


def sigmoid(z):
	'''
	z: (m, 1)

	Sigmoid = 1 / 1e(-z)
	'''
	return np.array([1 / (1 + math.exp(-x)) for x in z])


def predict(X, weights):
	return sigmoid(np.dot(X, weights))


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


def test(X_test, y_test, weights):
	predictions = [decision_boundary(prob) for prob in predict(X_test, weights)]
	return accuracy(predictions, y_test)


def one_vs_all(df, y_label, features, all):
	X = df.loc[:, features]
	X_test = X.sample(frac=0.3)
	X_train = X.loc[X.index.difference(X_test.index.values)]
	y_test, y_train = df.loc[X_test.index.values][y_label], df.loc[X_train.index.values][y_label]

	ret = {key: None for key in all}
	for one in all:
		ret[one] = train(X_train, y_train, one)

	for one in all:
		yh_test = np.where(y_test == one, 1, 0)
		accuracy = test(X_test, yh_test, np.array(ret[one]['weights']))
		print("for {}, accuracy of {}".format(one, accuracy))
	return [ret[one]['weights'] for one in all]


if __name__ == "__main__":

	features = get_features()

	file = "res/dataset_train.csv"
	dataset = read_file(file, ignore=True)
	df = normalize_df(pd.DataFrame(dataset[1:], columns=dataset[0]))
	weights = one_vs_all(df, 'Hogwarts House', features, get_houses())
	save_weights_into("weights", weights)
