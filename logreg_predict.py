#!/usr/bin/env python3
# coding: utf-8

import sys
import numpy as np
import pandas as pd
from tools import read_file, normalize_df
from hp_tools import get_features, get_houses
from LogisticRegressionOVA import LogisticRegressionOVA


def update_df(df, classifier):
	all = get_houses()
	X = df.loc[:, get_features()]
	log_reg = LogisticRegressionOVA()
	for i, one in enumerate(all):
		predictions = log_reg.set_weights(classifier[i]).predict(X)
		for index in np.where(predictions)[0]:
			df.ix[index, "Hogwarts House"] = one
	return log_reg


def load_classifier():
	try:
		classifier = [np.array(array) for array in np.load("classifier.npy")]
		return classifier
	except FileNotFoundError:
		print("Error: Train first before predicting")
		sys.exit(1)


if __name__ == "__main__":
	file = "res/dataset_test.csv"
	dataset = read_file(file, ignore=False)
	df = normalize_df(pd.DataFrame(dataset[1:], columns=dataset[0]))
	log_reg = update_df(df, load_classifier())
	df.to_csv("houses.csv", columns=["Hogwarts House"], index_label="Index")
