#!/usr/bin/env python3
#coding: utf-8


import sys
import matplotlib.pyplot as plt

from matrix import transpose
from hp_tools import sort_student_per_house, sort_marks_per_discipline
from tools import list_to_dict, read_file, normalize_dataset

def show_histogram(marks):
	fig, axes = plt.subplots(nrows=5, ncols=3, figsize=(20, 12))
	fig.canvas.set_window_title("Student marks depending on courses and houses")
	ax = axes.flatten()
	index = 0
	for discipline, values in marks.items():
		for house, average in values.items():
			ax[index].xaxis.set_ticklabels([])
			ax[index].yaxis.set_ticklabels([])
			ax[index].hist(average, label=house, bins=20, alpha=0.5)
			ax[index].set_title(discipline)
		index += 1
	handles, labels = ax[0].get_legend_handles_labels()
	plt.tight_layout()
	plt.legend(handles, labels, loc="best")
	plt.show()


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("usage: {} <csv_file>".format(__file__))
		sys.exit(-1)
	dataset_dict = list_to_dict(transpose(read_file(sys.argv[1])))
	if not any(dataset_dict['Hogwarts House']):
		print("`Hogwarts House` column empty")
		exit(1)
	dataset = normalize_dataset(dataset_dict)
	students = sort_student_per_house(dataset)
	marks = sort_marks_per_discipline([*dataset_dict.keys()][6:], students)
	show_histogram(marks)
