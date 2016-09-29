"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def get_number(tokens, index):
	"""returns number for arithmetic from string input"""
	if "." in tokens[index]:
		return float(tokens[index])
	else:
		return int(tokens[index])


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
			num1 = get_number(tokens, 1)
			if len(tokens) == 3:
				num2 = get_number(tokens, 2)
			operator = operator_type(tokens)
			if operator == "+":
				print add(num1, num2)
			elif operator == "-":
				print subtract(num1, num2)
			elif operator == "*":
				print multiply(num1, num2)
			elif operator == "/":
				print divide(num1, num2)
			elif operator == "square":
				print square(num1)
			elif operator == "cube":
				print cube(num1)
			elif operator == 'pow':
				print power(num1, num2)
			elif operator == 'mod':
				print mod(num1, num2)
		except (ValueError, UnboundLocalError, IndexError):
			print "That input was not valid. Please try again."


calc_shell()