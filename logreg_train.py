#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import pandas as pd
from hp_tools import get_houses, get_features
from tools import read_file, normalize_df
from LogisticRegressionOVA import LogisticRegressionOVA


if __name__ == "__main__":
	features = get_features()
	file = "res/dataset_train.csv"
	dataset = read_file(file, ignore=True)
	df = normalize_df(pd.DataFrame(dataset[1:], columns=dataset[0]))

	X = df.loc[:, features]
	y = df["Hogwarts House"]

	all = get_houses()
	log_reg = LogisticRegressionOVA().fit(X, y, one_vs_all=all)
	log_reg.save_classifier_into("classifier.npy")
