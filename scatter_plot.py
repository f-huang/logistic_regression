#!/usr/bin/env python3
#coding: utf-8

import sys
import math
import itertools
import matplotlib.pyplot as plt

from tools import list_to_dict, read_file
from hp_tools import sort_student_per_house, sort_marks_per_discipline
from matrix import transpose


def show_plot(marks):
	combinations = list(itertools.combinations(marks, 2))
	fig, axes = plt.subplots(nrows=4, ncols=math.ceil(len(combinations) / 4), figsize=(25, 10))
	fig.canvas.set_window_title("Look-alike features")
	ax = axes.flatten()
	number = 0
	for combination in combinations:
		ax[number].set_ylabel(combination[0])
		ax[number].set_xlabel(combination[1])
		for y_house, y_values in marks[combination[0]].items():
			for x_house, x_values in marks[combination[1]].items():
				if x_house == y_house:
					ax[number].scatter(x_values, y_values, label=y_house, alpha=0.5)
		number += 1
	handles, labels = ax[0].get_legend_handles_labels()
	plt.legend(handles, labels, loc="best")
	plt.show(fig)



if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("usage: {} <csv_file>".format(__file__))
		sys.exit(-1)
	dataset = read_file(sys.argv[1])
	dataset_dict = list_to_dict(transpose(dataset))
	students = sort_student_per_house(dataset)
	marks = sort_marks_per_discipline([*dataset_dict.keys()][6:], students)
	show_plot(marks)
