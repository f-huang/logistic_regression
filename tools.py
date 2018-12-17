#coding: utf-8

import csv


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
