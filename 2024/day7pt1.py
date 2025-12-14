from day7input import example_input

import operator
import itertools
from functools import reduce

op_code = {
	'+': operator.add,
	'*': operator.mul,
}

def equation_eval(operators, factors):
	"""
	Checks the sequence of operators
	"""
	ops = [''] + list(operators)
	equation_list = list(zip(ops, factors))

	# print(ops, factors, equation_list)
	return reduce(
		lambda acc, item: op_code[item[0]](acc, int(item[1])) if item[0] else int(item[1]), equation_list,
		0
	)
	

def check_row(line):
	"""
	Checks the row for possible solutions
	"""
	final_value = int(line[0])
	factors = list(map(int, line[1].split(' ')))

	operators_size = len(factors) - 1
	operations = itertools.product(op_code.keys(), repeat=operators_size)

	for operators in list(operations):
		if equation_eval(operators, factors) == final_value:
			# it can be equal
			return final_value


	return 0

if __name__ == '__main__':
	rows_evals = [check_row(line) for line in example_input]
	print('Result:', sum(rows_evals))
	assert( sum(rows_evals) == 3749 or 1545311493300)

