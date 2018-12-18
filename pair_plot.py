#!/usr/bin/env python3
#coding: utf-8

import sys
import itertools
import math
import matplotlib.pyplot as plt

from matrix import transpose
from hp_tools import sort_student_per_house, sort_marks_per_discipline
from tools import list_to_dict, read_file, normalize_dataset


def get_cartesian_set(list, repeat):
	ret = []
	for first in list:
		for second in list:
			ret.append((first, second))
	return ret


def show_pair_plot(marks):
	set = get_cartesian_set(marks, 2)
	fig, axes = plt.subplots(nrows=math.ceil(len(set) / 13), ncols=13, figsize=(25, 12))
	fig.canvas.set_window_title("Scatter plot matrix")
	ax = axes.flatten()
	for index, item in enumerate(set):
		ax[index].xaxis.set_ticklabels([])
		ax[index].yaxis.set_ticklabels([])
		if index % 13 == 0:
			ax[index].set_ylabel(item[0])
		if index > (len(set) / 12):
			ax[index].set_xlabel(item[1])
		if item[0] == item[1]:
			for house, values in marks[item[0]].items():
				ax[index].hist(values, label=house, bins=20, alpha=0.5)
		else:
			for y_house, y_values in marks[item[0]].items():
				for x_house, x_values in marks[item[1]].items():
					if x_house == y_house:
						ax[index].scatter(x_values, y_values, label=y_house, alpha=0.5)
	handles, labels = ax[0].get_legend_handles_labels()
	plt.tight_layout()
	plt.legend(handles, labels, loc="best")
	plt.show()


if __name__ == "__main__":
	file = "dataset_train.csv"
	dataset_dict = list_to_dict(transpose(read_file(file)))
	dataset = normalize_dataset(dataset_dict)
	students = sort_student_per_house(dataset)
	marks = sort_marks_per_discipline([*dataset_dict.keys()][6:], students)
	show_pair_plot(marks)
