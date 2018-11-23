#!/usr/bin/env python3
# coding: utf-8


import sys
import csv

from describe_tools import count, min, max, mean, quantile, std

def read_file(filename):
	try:
		with open(filename, 'r') as f:
			reader = csv.reader(f, delimiter=',')
			next(reader)
			dataset = [row for row in reader]
			return dataset
	except IOError:
		print("Cannot read this file: {}".format(filename))
		sys.exit(-1)


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("usage: {} <csv_file>".format(__file__))
		sys.exit(-1)
	filename = sys.argv[1]
	dataset = read_file(filename)
	data = [float(line[6]) if line[6] else 0.0 for line in dataset]
	print(min(data))
	print(max(data))
	print(mean(data))
	print(quantile(data, 25))
	print(std(data))
