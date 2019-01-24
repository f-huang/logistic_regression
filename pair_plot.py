#!/usr/bin/env python3
#coding: utf-8

import itertools
import math
import pandas as pd
import matplotlib.pyplot as plt

from hp_tools import get_houses, get_disciplines
from tools import preprocess

def get_cartesian_set(list, repeat):
	ret = []
	for first in list:
		for second in list:
			ret.append((first, second))
	return ret


def show_pair_plot(dataframes):
	cartesian_set = get_cartesian_set(get_disciplines(), 2)
	fig, axes = plt.subplots(nrows=math.ceil(len(cartesian_set) / 13), ncols=13, figsize=(25, 12))
	fig.canvas.set_window_title("Scatter plot matrix")
	ax = axes.flatten()
	for index, (discipline_1, discipline_2) in enumerate(cartesian_set):
		ax[index].xaxis.set_ticklabels([])
		ax[index].yaxis.set_ticklabels([])
		if index % 13 == 0:
			ax[index].set_ylabel(discipline_1)
		if index > (len(cartesian_set) / 12):
			ax[index].set_xlabel(discipline_2)
		[ax[index].hist(dataframes[house][discipline_1], bins=20, alpha=0.5, label=house)\
				if discipline_1 == discipline_2 else\
				ax[index].scatter(dataframes[house][discipline_1], dataframes[house][discipline_2], label=house, alpha=0.5)
			for house in get_houses()
		]
	handles, labels = ax[0].get_legend_handles_labels()
	plt.legend(handles, labels, loc="best")
	plt.show()


if __name__ == "__main__":
	file = "res/dataset_train.csv"
	df = preprocess(pd.read_csv(file, index_col="Index"))
	dataframes = {
		house: df[(df['Hogwarts House'] == house)]
		for house in get_houses()
	}
	show_pair_plot(dataframes)
