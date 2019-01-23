# coding: utf-8

import math
import numpy as np
import pandas as pd

class LogisticRegressionOVA():

	def __init__(self, n_iter = 1000, learning_rate = 12):
		self.n_iter = n_iter
		self.learning_rate = learning_rate
		self.cost_history = []
		self.weights = []
		self.classifier = []


	def __sigmoid(self, z):
		'''
		z: (m, 1)

		Sigmoid = 1 / 1e(-z)
		'''
		return np.array([1 / (1 + math.exp(-x)) for x in z])


	def __predict(self, X, weights):
		return self.__sigmoid(np.dot(X, weights))


	def __accuracy(self, my_y, his_y):
		diff = his_y == my_y
		return (np.count_nonzero(diff) / len(diff))


	def __decision_boundary(self, probability):
		return 1 if probability > 0.5 else 0

	def __cost_function(self, X, y):
		'''
		Using Cross-Entropy / Log Cross

		X: (m, 1)
		y: (m, 1)
		weights: (n, 1)
		Returns 1D matrix of predictions

		Cost = (y * log(predictions) + (1-y)*log(1-predictions)) / len(X)
		'''

		predictions = self.__predict(X, self.weights)
		cost_1 = -y * np.log(predictions)
		cost_2 = (1 - y) * np.log(1 - predictions)
		return (cost_1 - cost_2).sum() / len(X)


	def __update_weights(self, X, y):
		'''
		X: (m, 1)
		y: (m, 1)
		weights: (n, 1)
		'''

		predictions = self.__predict(X, self.weights)
		gradient = np.dot(X.T, predictions - y)
		self.weights = self.weights - gradient / len(X) * self.learning_rate


	def __fit(self, X, y):
		for _ in range(self.n_iter):
			self.__update_weights(X, y)
			cost = self.__cost_function(X, y)
			self.cost_history.append(cost)
		return self.weights


	def save_weights_into(self, path):
		np.save(path, self.weights)
		return self

	def save_classifier_into(self, path):
		np.save(path, self.classifier)
		return self


	def set_weights(self, weights):
		self.weights = weights
		return self


	def set_classifier(self, classifier):
		self.classifier = classifier
		return self


	def fit(self, X, y, one_vs_all=None):
		self.weights = np.array([0.0] * len(X.columns))
		if one_vs_all:
			self.classifier = [self.__fit(X, np.where(y == one, 1, 0)) for one in one_vs_all]
		else:
			self.classifier = self.__fit(X, y)
		return self


	def predict(self, X, one_vs_all=None):
		if (one_vs_all == None and len(self.weights) == 0) or (one_vs_all and len(self.classifier) == 0):
			raise Error("Fit first then predict.")
		if one_vs_all:
			predictions = {
				one: [prob for prob in self.__predict(X, self.classifier[i])]
				for i, one in enumerate(one_vs_all)
			}
			ret = []
			for i in range(len(X)):
				values = [predictions[one][i] for one in one_vs_all]
				ret += [one_vs_all[max_index] for max_index in [np.argmax(values)]]
			return ret
		else:
			return [self.__decision_boundary(prob) for prob in self.__predict(X, self.weights)]


	def score(self, X, y, one_vs_all=None):
		if one_vs_all:
			predictions = self.predict(X, one_vs_all)
			return self.__accuracy(predictions, y)
		else:
			predictions = self.predict(X)
			return self.__accuracy(predictions, y)
