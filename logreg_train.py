#!/usr/bin/env python3
# coding: utf-8

import sys
import math

from tools import read_file, list_to_dict, normalize_dataset
from matrix import transpose

## J(θ) = − (1/m) sum( yi log(hθ(xi)) + (1 − yi) log(1 − hθ(xi)))
## hθ(x) = g(θT x)
## g(z) = 1 / 1+e−z
## ∂ / ∂θj J(θ) =  1/m sum(hθ(xi) − yi)xij m i=1


def delta(list, h):
	return float(sum(h(x, y) for x, y in list) / len(list))


def get_sigmoid_function(z):
	return 1 / (1 + math.exp(-z))


def hypothesis(thetas, list_x):
	g = get_sigmoid_function
	return [x * theta for x in list_x for theta in thetas]

def train(dataset):
	thetas, learning_rate = [0.0] * len(dataset), 1.5
	i, cost = 0, 100
	# for index, row in enumerate(dataset):
		# g = get_sigmoid_function(thetas[index] * x)
		# thetas[index] -= learning_rate * delta(row, lambda x, y: (f(x)) - y * x)


if __name__ == "__main__":
	file = "dataset_train.csv"
	dataset_dict = list_to_dict(transpose(read_file(file)))
	dataset = normalize_dataset(dataset_dict)
	theta = train(dataset)
