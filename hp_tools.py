#coding: utf-8

from matrix import transpose


def sort_student_per_house(dataset):
	houses = ["Hufflepuff", "Slytherin", "Gryffindor", "Ravenclaw"]
	return {
		house: [student[6:] for student in dataset if student[1] == house]
		for house in houses
	}


def sort_marks_per_discipline(disciplines, students_per_house):
	marks = {}
	for house, students in students_per_house.items():
		for index, discipline in enumerate(disciplines):
			marks_per_discipline = transpose(students)
			values = [float(mark) if mark else 0.0 for mark in marks_per_discipline[index]]
			if disciplines[index] not in marks:
				marks[disciplines[index]] = {house: values}
			else:
				dictionnary = marks[disciplines[index]]
				dictionnary[house] = values
				marks[disciplines[index]] = dictionnary
	return marks

def get_disciplines():
	return [
		'Arithmancy',
		'Astronomy',
		'Herbology',
		'Defense Against the Dark Arts',
		'Divination',
		'Muggle Studies',
		'Ancient Runes',
		'History of Magic',
		'Transfiguration',
		'Potions',
		'Care of Magical Creatures',
		'Charms',
		'Flying'
	]

def get_houses():
	return ["Hufflepuff", "Slytherin", "Gryffindor", "Ravenclaw"]
