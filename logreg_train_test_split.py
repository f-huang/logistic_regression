#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import pandas as pd
from hp_tools import get_houses, get_features
from tools import preprocess
from LogisticRegressionOVA import LogisticRegressionOVA


if __name__ == "__main__":
	features = get_features()
	file = "res/dataset_train.csv"
	df = preprocess(pd.read_csv(file, index_col="Index"))

	y_label = "Hogwarts House"
	X = df.loc[:, features]
	X_test = X.sample(frac=0.3)
	X_train = X.loc[X.index.difference(X_test.index.values)]
	y_test, y_train = df.loc[X_test.index.values][y_label], df.loc[X_train.index.values][y_label]

	all = get_houses()
	log_reg = LogisticRegressionOVA().fit(X_train, y_train, one_vs_all=all)
	log_reg.save_classifier_into("classifier.npy")
	score = log_reg.score(X_test, y_test, one_vs_all=all)
	print("My score = {}".format(score))
