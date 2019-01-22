#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import pandas as pd
import math
from tools import read_file, normalize_df
from hp_tools import get_features, get_houses

def predict(X, weights):
	return sigmoid(np.dot(X, weights))

def accuracy(my_y, his_y):
	diff = his_y - my_y
	return 1 - (np.count_nonzero(diff)) / len(diff)


def sigmoid(z):
	'''
	z: (m, 1)

	Sigmoid = 1 / 1e(-z)
	'''
	return np.array([1 / (1 + math.exp(-x)) for x in z])


def decision_boundary(probability):
	return 1 if probability > 0.5 else 0

if __name__ == "__main__":
	file = "res/dataset_test.csv"
	y_label = "Hogwarts House"
	dataset = read_file(file, ignore=False)
	df = normalize_df(pd.DataFrame(dataset[1:], columns=dataset[0]))
	weights = [np.array(array) for array in np.load("weights.npy")]
	X = df.loc[:, get_features()]
	for i, house in enumerate(get_houses()):
		predictions = [decision_boundary(prob) for prob in predict(X, weights[i])]
		indexes = np.where(predictions)[0]
		for index in indexes:
			df.ix[index, y_label] = house
	df.to_csv("houses.csv", columns=[y_label], index_label="Index")
