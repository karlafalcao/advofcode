import re
import functools
import pprint
file = open('day6input.txt')
input_r = file.read()
file.close()

input = R"""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

ops_list = [re.split(r"\s+", x.strip()) for x in input_r.split('\n')]
ops_list = ops_list[:-1]
pprint.pprint(ops_list)
print(len(ops_list[0]))
print(len(ops_list))
print(ops_list[4])

current_operands = []
operation = ''

import operator

operations = {
	'*': operator.mul,
	'+': operator.add
}

total_sum = 0
for col_idx in range(len(ops_list[0])):
	print('col_idx', col_idx)
	for row_idx in range(len(ops_list)):
		print('row_idx', row_idx)
		cel = ops_list[row_idx][col_idx]
		print('cel:', cel)
		if cel in operations.keys():
			operator = operations[cel]
			
			result = functools.reduce(lambda x,y: operator(x,y), current_operands)
			total_sum += result
			print('result', result)
			current_operands = []
		else:
			current_operands.append(int(cel))

print(total_sum)



