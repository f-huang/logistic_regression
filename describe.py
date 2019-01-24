#!/usr/bin/env python3
# coding: utf-8


import sys
import csv
import pandas as pd
from tools import is_number
from ft_math import count, min, max, mean, quantile, std


def output(initial_df, standardized_df):
	print("%-10s"%" ", "| ".join("%20s"%(feature[:18] + ".." if len(feature) > 18 else feature) for feature in standardized_df.columns))
	print("%-10s"%"Total", "| ".join("%20i"%(count(initial_df[column])) for column in initial_df))
	print("%-10s"%"CountNaN", "| ".join("%20i"%(count(initial_df[column]) - count(standardized_df[column])) for column in initial_df))
	print("%-10s"%"Count", "| ".join("%20i"%(count(standardized_df[column])) for column in standardized_df))
	print("%-10s"%"Mean","| ".join("%20.6f"%(mean(standardized_df[column])) for column in standardized_df))
	print("%-10s"%"Std","| ".join("%20.6f"%(std(standardized_df[column])) for column in standardized_df))
	print("%-10s"%"Min","| ".join("%20.6f"%(min(standardized_df[column])) for column in standardized_df))
	print("%-10s"%"25%","| ".join("%20.6f"%(quantile(standardized_df[column], 25)) for column in standardized_df))
	print("%-10s"%"50%","| ".join("%20.6f"%(quantile(standardized_df[column])) for column in standardized_df))
	print("%-10s"%"75%","| ".join("%20.6f"%(quantile(standardized_df[column], 75)) for column in standardized_df))
	print("%-10s"%"Max","| ".join("%20.6f"%(max(standardized_df[column])) for column in standardized_df))


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("usage: {} <csv_file>".format(__file__))
		sys.exit(-1)
	filename = sys.argv[1]
	initial_df = pd.read_csv(filename, index_col="Index").dropna(how='all', axis=1).select_dtypes(['float64', 'int'])
	standardized_df = initial_df.dropna()
	output(initial_df, standardized_df[[c for c in standardized_df.columns if is_number(standardized_df[c][0])]])
