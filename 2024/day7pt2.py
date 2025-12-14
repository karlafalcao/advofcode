from day7pt1 import op_code, check_row, example_input, operator

if __name__ == '__main__':
	op_code['||'] = lambda acc, val: int(operator.concat(str(acc), str(val))) # Partt2
	rows_evals = [check_row(line) for line in example_input]

	print('Result:', sum(rows_evals))

	assert(sum(rows_evals) == 11387 or 169122112716571)
