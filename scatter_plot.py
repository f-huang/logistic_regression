#!/usr/bin/env python3
#coding: utf-8

import math
import itertools
import pandas as pd
import matplotlib.pyplot as plt

from tools import read_file
from hp_tools import get_houses, get_disciplines


def show_plot(dataframes):
	combinations = list(itertools.combinations(get_disciplines(), 2))
	fig, axes = plt.subplots(nrows=6, ncols=math.ceil(len(combinations) / 6), figsize=(25, 12))
	fig.canvas.set_window_title("Look-alike features")
	ax = axes.flatten()
	for index, (discipline_1, discipline_2) in enumerate(combinations):
		ax[index].set_xlabel(discipline_1)
		ax[index].set_ylabel(discipline_2)
		ax[index].xaxis.set_ticklabels([])
		ax[index].yaxis.set_ticklabels([])
		[ax[index].scatter(dataframes[house][discipline_1], dataframes[house][discipline_2], label=house, alpha=0.5)
			for house in get_houses()
		]
	handles, labels = ax[0].get_legend_handles_labels()
	plt.legend(handles, labels, loc="best")
	plt.show(fig)


if __name__ == "__main__":
	file = "dataset_train.csv"
	dataset = read_file(file)
	df = pd.DataFrame(dataset[1:], columns=dataset[0])
	dataframes = {
		house: df[(df['Hogwarts House'] == house)]
		for house in get_houses()
	}
	show_plot(dataframes)
