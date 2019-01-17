#!/usr/bin/env python3
#coding: utf-8


import sys
import pandas as pd
import matplotlib.pyplot as plt

from hp_tools import get_houses, get_disciplines
from tools import list_to_dict, read_file, normalize_df


def show_histogram(dataframes):
	fig, axes = plt.subplots(nrows=5, ncols=3, figsize=(20, 12))
	fig.canvas.set_window_title("Student marks depending on courses and houses")
	ax = axes.flatten()
	for index, discipline in enumerate(get_disciplines()):
		for house, df_house in dataframes.items():
			ax[index].hist(df_house[discipline], label=house, bins=20, alpha=0.5)
			ax[index].set_title(discipline)
			ax[index].xaxis.set_ticklabels([])
			ax[index].yaxis.set_ticklabels([])
	handles, labels = ax[0].get_legend_handles_labels()
	plt.tight_layout()
	plt.legend(handles, labels, loc="best")
	plt.show()


if __name__ == "__main__":
	file = "dataset_train.csv"
	dataset = read_file(file)
	df = pd.DataFrame(dataset[1:], columns=dataset[0])
	dataframes = {
		house: df[(df['Hogwarts House'] == house)]
		for house in get_houses()
	}
	show_histogram(dataframes)
