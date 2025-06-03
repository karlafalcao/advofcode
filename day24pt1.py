file = open('day24example.txt', 'r')
file = open('day24input.txt', 'r')
file_content = file.read()
file.close()


gates = dict()
def add_gate(gate_line):
	print(gate_line)
	if not len(gate_line): return
	gate = gate_line.split(': ')
	gates[gate[0]] = int(gate[1])


wires = []
wires_dict = dict()

def parse_wire(wire_line):
	if (not wire_line): return ()
	x, operator, y, z = wire_line.replace(' -> ', ' ').split()
	wires_dict[z] = (operator, x, y)
	return x, operator, y, z

def add_wire(wire_line):
	parsed_wire = parse_wire(wire_line)
	if parsed_wire and not solve_wire(parsed_wire):
		wires.append(parsed_wire)

import operator
operations = {
	'AND': operator.and_,
	'OR': operator.or_,
	'XOR': operator.xor
}
z_gates = dict()

def solve_it(x, y, operator):
	op_eval_fn = operations[operator]
	return op_eval_fn(x, y)

def solve_wire(wire):
	x, operator, y, z  = wire

	if (x in gates and y in gates):
		op_eval = solve_it(
			int(gates[x]),
			int(gates[y]),
			operator
		)
		gates[z] = op_eval
		
		if z.startswith('z'):
			z_gates[z] = op_eval

		return True

	return False

def recursive_wire(wires):
	for wire in wires:
		if solve_wire(wire):
			wires.remove(wire)

	if len(wires):
		recursive_wire(wires)

def solve_gates():
	[add_gate(line) if ':' in line else add_wire(line) for line in file_content.split('\n') ]
	print('wires: ', wires)
	recursive_wire(wires)
	print('gates: ', gates)

	# {'z15': 0, 'z00': 0, 'z01': 1, 'z02': 1, 'z03': 0, 'z04': 0, 'z06': 0, 'z05': 0, 'z07': 0, 'z08': 1, 'z09': 1, 'z10': 0, 'z11': 1, 'z12': 0, 'z13': 0, 'z14': 1, 'z16': 1, 'z17': 0, 'z18': 0, 'z19': 1, 'z20': 1, 'z21': 0, 'z22': 1, 'z23': 0, 'z24': 0, 'z25': 1, 'z26': 1, 'z27': 0, 'z28': 1, 'z29': 1, 'z30': 0, 'z31': 0, 'z32': 0, 'z33': 1, 'z34': 0, 'z35': 1, 'z36': 1, 'z37': 0, 'z38': 1, 'z39': 0, 'z40': 1, 'z42': 0, 'z41': 1, 'z43': 1, 'z44': 0, 'z45': 1}
	z_gates_keys_ordered = sorted(z_gates, reverse=True)
	sorted_z_gates = ''.join([str(z_gates[val]) for val in z_gates_keys_ordered])

	print('z_gates: ', z_gates)
	solution = int(sorted_z_gates, 2)
	print('The binary solution converted to decimal is:', solution)
	assert (solution, 47666458872582)

solve_gates()
