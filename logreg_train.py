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

	X = df.loc[:, features]
	y = df["Hogwarts House"]

	all = get_houses()
	log_reg = LogisticRegressionOVA().fit(X, y, one_vs_all=all)
	log_reg.save_classifier_into("classifier.npy")
