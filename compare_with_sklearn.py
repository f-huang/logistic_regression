#!/usr/bin/env python3

from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler

import pandas as pd
from hp_tools import get_features

def compare(sk_predictions):
	my_predictions = pd.read_csv("houses.csv", index_col="Index")
	diff = (my_predictions == sk_predictions)
	n_rows_identical = len(diff[diff["Hogwarts House"] == True])
	print("Accuracy = {}%".format(n_rows_identical / len(diff) * 100))


if __name__ == "__main__":
	features = get_features()
	sc = StandardScaler()

	df_train = pd.read_csv("res/dataset_train.csv", index_col="Index").dropna()
	X_train = sc.fit_transform(df_train.loc[:, features])
	y_train = df_train["Hogwarts House"]

	df_test = pd.read_csv("res/dataset_test.csv", index_col="Index").drop(["Hogwarts House"], axis=1).dropna()
	X_test = sc.fit_transform(df_test.loc[:, features])

	predictions = OneVsOneClassifier(LinearSVC()).fit(X_train, y_train).predict(X_test)
	sk_predictions = pd.DataFrame(predictions, index=df_test.index, columns=["Hogwarts House"])
	sk_predictions.to_csv("sk_houses.csv", index_label="Index", columns=["Hogwarts House"])
	compare(sk_predictions)
