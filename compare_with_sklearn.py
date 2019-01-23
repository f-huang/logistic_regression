#!/usr/bin/env python3

from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

import pandas as pd
from hp_tools import get_features


if __name__ == "__main__":
	features = get_features()
	sc = StandardScaler()

	df_train = pd.read_csv("res/dataset_train.csv", index_col="Index").dropna()
	X_train = sc.fit_transform(df_train.loc[:, features])
	y_train = df_train["Hogwarts House"]

	df_test = pd.read_csv("res/dataset_test.csv", index_col="Index").drop(["Hogwarts House"], axis=1).dropna()
	X_test = sc.fit_transform(df_test.loc[:, features])

	predictions = OneVsOneClassifier(LinearSVC()).fit(X_train, y_train).predict(X_test)
	my_predictions = pd.read_csv("houses.csv", index_col="Index")
	sk_predictions = pd.DataFrame(predictions, index=df_test.index, columns=["Hogwarts House"])

	sk_predictions.to_csv("sk_houses.csv", index_label="Index", columns=["Hogwarts House"])

	print("Accuracy = {}%".format(accuracy_score(sk_predictions, my_predictions) * 100))
