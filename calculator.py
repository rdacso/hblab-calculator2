"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def get_number(num_only):
	"""returns number for arithmetic from string input"""
	num_for_math = []
	for item in num_only:
		if "." in item:
			num_for_math.append(float(item))
		else:
			num_for_math.apspend(int(item))
	return num_for_math

def my_reduce(function, iterable):
	


def operator_type(tokens):
	"""returns operator type for arithmetic from string input"""
	return tokens[0]

def calc_shell():
	"""Enter operator and equivalent number of integers to calculate answer. Press q to quit"""
	while True:
		try:
			calc_input = raw_input("Please enter a mathematical equation. ").lower()
			tokens = calc_input.split(' ')
			if tokens[0] == "q":
				break
			num1_not_transformed = tokens[1]
			if '.' in num1_not_transformed:
				num1 = float(num1_not_transformed)
			else:
				num1 = int(num1_not_transformed)
			if len(tokens) > 2:
				nums_final = get_number(num_only)
			num_only = tokens[1:]
			operator = operator_type(tokens)
			if operator == "+":
				addition = reduce(add, nums_final)
				print "%.2f" % (addition)
			elif operator == "-":
				subtracting = reduce(subtract, nums_final)
				print "%.2f" % (subtracting)
			elif operator == "*":
				multiplying = reduce(multiply, nums_final)
				print "%.2f" % (multiplying)
			elif operator == "/":
				division = reduce(divide, nums_final)
				print "%.2f" % (division)
			elif operator == "square":
				squaring = square(num1)
				print "%.2f" % (squaring)
			elif operator == "cube":
				cubed = cube(num1)
				print "%.2f" % (cubed)
			elif operator == 'pow':
				powered = reduce(power, nums_final)
				print "%.2f" % (powered)
			elif operator == 'mod':
				modular = reduce(mod, nums_final)
				print "%.2f" % (modular)
		except (ValueError, UnboundLocalError, IndexError):
			print "That input was not valid. Please try again."


calc_shell()