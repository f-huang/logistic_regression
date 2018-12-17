#!/usr/bin/env python3
# coding: utf-8


import sys
import csv

from tools import is_number, read_file
from ft_math import count, min, max, mean, quantile, std
from matrix import transpose


def standardize_dataset(dataset):
	ret = []
	for row in dataset:
		if row[0] != "Index" and is_number(row[1]):
			ret.append([row[0]] + [float(value) if value else 0.0 for value in row[1:]])
	return ret


def output(original, data):
	print("%-10s"%" ", "| ".join("%20s"%(feature[:18] + ".." if len(feature) > 18 else feature) for feature in original[0]))
	print("%-10s"%"Count", "| ".join("%20i"%(count(list[1:])) for list in data))
	print("%-10s"%"Mean","| ".join("%20.6f"%(mean(list[1:])) for list in data))
	print("%-10s"%"Std","| ".join("%20.6f"%(std(list[1:])) for list in data))
	print("%-10s"%"Min","| ".join("%20.6f"%(min(list[1:])) for list in data))
	print("%-10s"%"25%","| ".join("%20.6f"%(quantile(list[1:], 25)) for list in data))
	print("%-10s"%"50%","| ".join("%20.6f"%(quantile(list[1:])) for list in data))
	print("%-10s"%"75%","| ".join("%20.6f"%(quantile(list[1:], 75)) for list in data))
	print("%-10s"%"Max","| ".join("%20.6f"%(max(list[1:])) for list in data))


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("usage: {} <csv_file>".format(__file__))
		sys.exit(-1)
	filename = sys.argv[1]
	original_data = transpose(read_file(filename))
	transposed = standardize_dataset(original_data)
	output(transpose(transposed), transposed)
