#coding: utf-8

import csv

import sys
import pandas as pd
from ft_math import max, min, normalize, unnormalize

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


def read_file(filename, ignore=False):
	try:
		with open(filename, 'r') as f:
			reader = csv.reader(f, delimiter=',')
			# next(reader)
			return (list(filter(lambda row: None not in row,
				[[float(item) if is_float(item) else (item if item else None)
					for item in row
				] for row in reader]))) if ignore\
				else [[float(item) if item and is_float(item)\
					else (item if item else 0.0)
					for item in row]
				for row in reader]
	except IOError:
		print("Cannot read this file: {}".format(filename))
		sys.exit(-1)


def normalize_list(list):
	maximum, minimum = (max(list), min(list))
	return [normalize(item, maximum, minimum)\
		if item and isinstance(item, (int, float)) else item for item in list]

def normalize_df(df):
	for column, values in df.iteritems():
		df[column] = normalize_list(df[column]) \
		if len(list(filter(lambda item: isinstance(item, str), values))) == 0\
		else df[column]
	return df


def preprocess(df, converter=lambda x: x, drop_columns=[]):
	return normalize_df(df.drop(drop_columns, axis=1).dropna())
