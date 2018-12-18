#coding: utf-8

import csv

from ft_math import max, min, normalize
from matrix import transpose

def is_number(string):
	try:
		float(string)
		return True
	except ValueError:
		return False


def list_to_dict(list, key_index = 0):
	return {
		row[key_index]: row[1:]
		for row in list
	}

def is_float(value):
	try:
		float(value)
		return True
	except ValueError:
		return False


def read_file(filename):
	try:
		with open(filename, 'r') as f:
			reader = csv.reader(f, delimiter=',')
			# next(reader)
			dataset = [[float(item) if item and is_float(item) else (item if item else 0.0) for item in row] for row in reader]
			return dataset
	except IOError:
		print("Cannot read this file: {}".format(filename))
		sys.exit(-1)


def normalize_list(list):
	maximum, minimum = (max(list), min(list))
	return [normalize(item, maximum, minimum)\
		if item and isinstance(item, (int, float)) else item for item in list]


def unnormalize_list(list):
	maximum, minimum = (max(list), min(list))
	return [unnormalize(item, maximum, minimum)\
		if item and isinstance(item, (int, float)) else item for item in list]


def normalize_dataset(dict):
	dataset = []
	for key, values in dict.items():
		if len(list(filter(lambda item: isinstance(item, str), values))) == 0:
			dataset.append(normalize_list(values))
		else:
			dataset.append(values)
	return transpose(dataset)
