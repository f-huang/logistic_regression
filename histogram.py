#!/usr/bin/env python3
#coding: utf-8


import sys
import csv
import matplotlib.pyplot as plt

from matrix import transpose
from ft_math import mean

def read_file(filename):
	try:
		with open(filename, 'r') as f:
			reader = csv.reader(f, delimiter=',')
			# next(reader)
			dataset = [row for row in reader]
			return dataset
	except IOError:
		print("Cannot read this file: {}".format(filename))
		sys.exit(-1)


def show_histogram(marks):
	fig, axes = plt.subplots(nrows=5, ncols=3)
	ax = axes.flatten()
	index = 0
	for discipline, values in marks.items():
		print(discipline, ":")
		print("\n".join("\t%s: %s"%(house, value) for house, value in values.items()))
		for house, average in values.items():
			ax[index].hist(average, label=house)
			ax[index].set_title(discipline)
		index += 1
	plt.legend(loc="best")
	plt.show()



def get_student_average_marks(disciplines, students_per_house):
	# marks = {}
	# for house, students in students_per_houses.items():
	# 	marks_per_house = transpose(students)
	# 	marks[house] = [mean([float(mark) if mark else 0.0 for mark in discipline]) for discipline in marks_per_house]
	# for house, averages in marks.items():
	# 	print("{}: {}\n".format(house, averages))
	# 	plt.hist(averages, label=house)
	marks = {}
	for house, students in students_per_house.items():
		for index, discipline in enumerate(disciplines):
			marks_per_house = transpose(students)
			values = mean([float(mark) if mark else 0.0 for mark in marks_per_house[index]])
			if disciplines[index] not in marks:
				marks[disciplines[index]] = {house: values}
			else:
				dictionnary = marks[disciplines[index]]
				dictionnary[house] = values
				marks[disciplines[index]] = dictionnary
	return marks


def sort_marks_per_discipline(disciplines, students_per_house):
	marks = {}
	for house, students in students_per_house.items():
		for index, discipline in enumerate(disciplines):
			marks_per_discipline = transpose(students)
			values = [mark for mark in marks_per_discipline]
			if disciplines[index] not in marks:
				marks[disciplines[index]] = values
			else:
				list = marks[disciplines[index]]
				list.extend(values)
				marks[disciplines[index]] = list
	return marks


def sort_student_per_house(dataset):
	houses = ["Hufflepuff", "Slytherin", "Gryffindor", "Ravenclaw"]
	return {
		house: [student[6:] for student in dataset if student[1] == house]
		for house in houses
	}


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("usage: {} <csv_file>".format(__file__))
		sys.exit(-1)
	dataset = read_file(sys.argv[1])
	disciplines = [feature[0] for feature in transpose(dataset)[6:]]
	students = sort_student_per_house(dataset)
	# marks = sort_marks_per_discipline(disciplines, students)
	marks = get_student_average_marks(disciplines, students)
	show_histogram(marks)
