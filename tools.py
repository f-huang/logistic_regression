#coding: utf-8


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
