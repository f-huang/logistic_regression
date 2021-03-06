# coding: utf-8

def count(list):
	return len(list)


def min(iterable, key = lambda x: x, default = 0):
		if len(iterable) == 0:
			raise ValueError("Argument `iterable`'s length should be at least 1.")
		ret = default
		for elem in iterable:
			if key(ret) > key(elem) :
				ret = elem
		return ret

def max(iterable, key = lambda x: x, default = 0):
	if len(iterable) == 0:
		raise ValueError("Argument `iterable`'s length should be at least 1.")
	ret = default
	for elem in iterable:
		if key(ret) < key(elem) :
			ret = elem
	return ret


# def max(arg1, arg2, *args, key = lambda x: x):
# 	return max([arg1, arg2, *args], key=key)


def mean(list):
	return float(sum(list) / max([len(list), 1]))


def quantile(list, percent = 50):
	if percent < 0 or percent > 100:
		raise ValueError("Argument `percent` should be between 0 and 100")
	elif len(list) == 0:
		raise ValueError("Argument `list` is empty")
	return sorted(list)[int(percent / 100 * (len(list) - 1))]


def std(list):
	if len(list) == 0:
		raise ValueError("Argument `list` is empty")
	average = mean(list)
	return ((float(sum((element - average)**2 for element in list))) / max([len(list) - 1, 1])) ** (1/2.0)


def normalize(value, max, min):
	return (value - min) / (max - min)


def unnormalize(value, max, min):
	return value * (max - min) + min
