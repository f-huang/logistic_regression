#!/usr/bin/env python3
# coding: utf-8


import sys
import csv
import pandas as pd
from tools import is_number, read_file
from ft_math import count, min, max, mean, quantile, std


def output(df):
	print("%-10s"%" ", "| ".join("%20s"%(feature[:18] + ".." if len(feature) > 18 else feature) for feature in df.columns))
	print("%-10s"%"Count", "| ".join("%20i"%(count(df[column])) for column in df))
	print("%-10s"%"Mean","| ".join("%20.6f"%(mean(df[column])) for column in df))
	print("%-10s"%"Std","| ".join("%20.6f"%(std(df[column])) for column in df))
	print("%-10s"%"Min","| ".join("%20.6f"%(min(df[column])) for column in df))
	print("%-10s"%"25%","| ".join("%20.6f"%(quantile(df[column], 25)) for column in df))
	print("%-10s"%"50%","| ".join("%20.6f"%(quantile(df[column])) for column in df))
	print("%-10s"%"75%","| ".join("%20.6f"%(quantile(df[column], 75)) for column in df))
	print("%-10s"%"Max","| ".join("%20.6f"%(max(df[column])) for column in df))


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("usage: {} <csv_file>".format(__file__))
		sys.exit(-1)
	filename = sys.argv[1]
	dataset = read_file(filename)
	df = pd.DataFrame(dataset[1:], columns=dataset[0])
	output(df[[c for c in df.columns if is_number(df[c][0])]])
