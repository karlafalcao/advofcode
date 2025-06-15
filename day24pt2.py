file = open('day24example.txt', 'r')
file = open('day24input.txt', 'r')
file_content = file.read()
file.close()


gates = dict()
def add_gate(gate_line):
	if not len(gate_line): return
	gate_key, gate_val = gate_line.split(': ')
	gates[gate_key] = int(gate_val)


wires_dict = dict()
wires = []

def add_wire(wire_line):
	if not wire_line: return ()
	x, operator, y, z = wire_line.replace(' -> ', ' ').split()

	wires_dict[z] = (operator, x, y)
	wires.append((x, operator, y, z))
	return x, operator, y, z
#
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

def parse_file_line(line):
	add_gate(line) if ':' in line else add_wire(line)

def solve_gates(wires):
	expected_dict = {'z15': 0, 'z00': 0, 'z01': 1, 'z02': 1, 'z03': 0, 'z04': 0,
	'z06': 0, 'z05': 0, 'z07': 0, 'z08': 1, 'z09': 1, 'z10': 0,
	'z11': 1, 'z12': 0, 'z13': 0, 'z14': 1, 'z16': 1, 'z17': 0,
	'z18': 0, 'z19': 1, 'z20': 1, 'z21': 0, 'z22': 1, 'z23': 0,
	'z24': 0, 'z25': 1, 'z26': 1, 'z27': 0, 'z28': 1, 'z29': 1,
	'z30': 0, 'z31': 0, 'z32': 0, 'z33': 1, 'z34': 0, 'z35': 1,
	'z36': 1, 'z37': 0, 'z38': 1, 'z39': 0, 'z40': 1, 'z42': 0,
	'z41': 1, 'z43': 1, 'z44': 0, 'z45': 1}
	recursive_wire(wires)

	z_gates_keys_ordered = sorted(z_gates, reverse=True)
	sorted_z_gates = ''.join([str(z_gates[val]) for val in z_gates_keys_ordered])

	print('z_gates: ', z_gates)
	assert expected_dict, z_gates
	solution = int(sorted_z_gates, 2)
	print('The binary solution converted to decimal is:', solution)
	assert solution, 47666458872582


def build_wires():
	[parse_file_line(line) for line in file_content.split('\n') ]
	# print('gates: ', gates)
	# print('wires: ', wires)
	# print('wires_dict: ', wires_dict)

def pp(wire, depth=0):
	if wire[0] in 'xy': return '  ' * depth + wire # Base case for x and y wires
	op, x, y = wires_dict[wire]
	return '  ' * depth + op + '"' + wire + '"' + '\n' + pp(x, depth + 1) + '\n' + pp(y, depth + 1)

build_wires()

solve_gates(wires)
result = pp("z45")
print('Resulting wire structure:\n', result)

# Bitwise SUM Formula (add two binary numbers x and y)

# # Edge cases

# # First carry ever is a x00 AND y00 only
# ('y00 AND x00 -> rpj',)

# # First value is x00 XOR y00 only
# ('x00 XOR y00 -> z00',)

## Second value has a simple previous carry
# XOR"z01"
# AND"rpj"
# y00
# x00
# XOR"nsc"
# y01
# x01
# # Last value the carry is the final result bit
# 'mgq OR nng -> z45',

# 'y22 XOR x22 -> kqm',

# # previous carry
# 'wff AND kqm -> vgf', recarry
# 'x22 AND y22 -> bkn', direct carry
# 'vgf OR bkn -> ggg', carry bit

# # intermediate XOR
# 'x23 XOR y23 -> gjq',

# # Result value
# 'ggg XOR gjq -> z23', z Formula XOR

# # next carry calculus
# 'gjq AND ggg -> tqq', recarry
# 'x23 AND y23 -> ctb', direct carry
# 'tqq OR ctb -> qsv', carry bit

# # Result value
# 'x24 XOR y24 -> ___', intermediate XOR
# 'qsv XOR ___ -> z24', z Formula XOR

# ...
# 'qsv AND ___ -> ', rc
# 'x24 AND y24 -> ',dc


#### ---- WRONG WIRES: NOT WELL-FORMED FORMULAS

# 'y15 AND x15 -> z15',
# 'vhr XOR dvj('x15 XOR y15 -> dvj') -> dnt'

# 'sgt OR bhb -> z05'
# 'ggh XOR tvp('y05 XOR x05 -> tvp') -> jst'

# 'kgr AND vrg -> z30',
# 'kgr XOR vrg('x30 XOR y30 -> vrg') -> gwc'

# 'x10 AND y10 -> mcm'
# 'y10 XOR x10 -> gdf'
# 'mcc OR hrq -> tdw',
# 'mcm(should be XOR but its AND) XOR tdw(Should be OR) -> z10'
print('Puzzle answer is dnt,gdf,gwc,jst,mcm,z05,z15,z30') 

