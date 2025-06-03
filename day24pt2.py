# x00: 1 y00: 1 z00: 0
# x01: 0 y01: 1 z01: 0
# x02: 1 y02: 1 z02: 0
# x03: 1 y03: 1 z03: 1
# x04: 0 y04: 1 z04: 0
# 				z05: 1

# bitwise and (X, Y)
# x00: 1 y00: 1 z00: 0
# x01: 1 y01: 0 z01: 0
# x02: 0 y02: 1 z02: 0
# x03: 1 y03: 1 z03: 1
# 			  z04: 1

# valid_equations:  ['x25 AND y25 -> djr', 'x12 AND y12 -> htp', 'x35 AND y35 -> fqm', 
# 'x03 AND y03 -> vvj', 'x27 AND y27 -> mjw', 'y18 AND x18 -> dwt', 'y38 AND x38 -> cpg', 
# 'y19 AND x19 -> gth', 'y40 AND x40 -> fqs', 'y39 AND x39 -> dqk', 'y36 AND x36 -> gdr', 
# 'y17 AND x17 -> ppv', 'x10 AND y10 -> mcm', 'y14 AND x14 -> hdb', 'x23 AND y23 -> ctb', 
# 'x03 AND y03 -> vvj', 'y42 AND x42 -> tcm', 'y24 AND x24 -> wck', 'x07 AND y07 -> qrm', 
# 'y09 AND x09 -> hrq', 'y15 AND x15 -> z15', 'x29 AND y29 -> cfp', 'y08 AND x08 -> njd', 
# 'y31 AND x31 -> vbc', 'x32 AND y32 -> gdg', 'x33 AND y33 -> vmf', 'y21 AND x21 -> ffj', 
# 'y01 AND x01 -> bkg', 'y11 AND x11 -> dnh', 'y13 AND x13 -> gns', 'y16 AND x16 -> tjw', 
# 'y30 AND x30 -> fhg', 'x41 AND y41 -> pfn', 'y00 AND x00 -> rpj', 'x20 AND y20 -> hbf', 
# 'y37 AND x37 -> fdg', 'x44 AND y44 -> nng', 'x22 AND y22 -> bkn', 'x28 AND y28 -> mtc', 
# 'y06 AND x06 -> fsb', 'x04 AND y04 -> kff', 'y26 AND x26 -> pvv', 'x02 AND y02 -> vgh', 
# 'y43 AND x43 -> csh', 'y34 AND x34 -> hrg', 'kgr AND vrg -> z30']
# 'y00 AND x00 -> rpj',
# 'y01 AND x01 -> bkg',
# 'x02 AND y02 -> vgh'
# 'x03 AND y03 -> vvj'
# 'x04 AND y04 -> kff'
# 'y06 AND x06 -> fsb'


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

def pp(wire, depth=0):
	if wire[0] in 'xy': return ' ' * depth + wire
	op, x, y = wires_dict[wire]
	return ' ' * depth + op + wire + '\n' + pp(x, depth + 1) + '\n' + pp(y, depth + 1)


def solve_gates():
	[add_gate(line) if ':' in line else add_wire(line) for line in file_content.split('\n') ]
	print('wires: ', wires)
	print(wires_dict)

	assert (solution, 47666458872582)


pp("z00")
# 'y22 XOR x22 -> kqm',

# # previous carry
# 'wff AND kqm -> vgf',
# 'x22 AND y22 -> bkn',
# 'vgf OR bkn -> ggg', carry bit

# # Result value
# 'x23 XOR y23 -> gjq', intermediate XOR
# 'ggg XOR gjq -> z23', z Formula XOR

# # next carry calculus
# 'gjq AND ggg -> tqq', recarry
# 'x23 AND y23 -> ctb', direct carry
# 'tqq OR ctb -> qsv', carry bit

# # Result value
# 'x24 XOR y24 -> ___', intermediate XOR
# 'qsv XOR ___ -> z24', z Formula XOR

# 'qsv AND ___ -> ', rc
# 'x24 AND y24 -> ',dc

# # Edge cases

# # First carry is a x00 AND y00 only
# ('y00 AND x00 -> rpj',)
# # First value is x00 XOR y00 only 
# ('x00 XOR y00 -> z00',)

# # Last value the carry is the final result bit
# 'mgq OR nng -> z45',

#### ---- WRONG WIRES: NOT WELL FORMED FORMULAS

# 'y15 AND x15 -> z15',
# 'vhr XOR dvj('x15 XOR y15 -> dvj') -> dnt'

# 'sgt OR bhb -> z05'
# 'ggh XOR tvp('y05 XOR x05 -> tvp') -> jst'

# 'kgr AND vrg -> z30',
# 'kgr XOR vrg('x30 XOR y30 -> vrg') -> gwc'

# 'x10 AND y10 -> mcm'
# 'y10 XOR x10 -> gdf'
# 'mcc OR hrq -> tdw',
# 'mcm(should be a XOR but its and AND) XOR tdw(Should be an OR) -> z10'
print('Puzzle answer is dnt,gdf,gwc,jst,mcm,z05,z15,z30') 

