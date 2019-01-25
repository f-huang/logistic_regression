#coding: utf-8

import csv

import sys
import pandas as pd
from ft_math import max, min, mean, normalize

def is_number(string):
	try:
		float(string)
		return True
	except ValueError:
		return False


def is_float(value):
	try:
		float(value)
		return True
	except ValueError:
		return False


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


def convert_nan(df, converter=0.0):
	return df.fillna(converter)


def preprocess(df, drop_columns=[]):
	dropped = df.dropna()
	means = {c: mean(dropped[c]) for c in dropped.columns}
	return normalize_df(convert_nan(df.drop(drop_columns, axis=1), means))
