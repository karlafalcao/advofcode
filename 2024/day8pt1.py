from day8input import day8input

# print(day8input)

# check the matrix for antennas of same frequency
# 
# navigate thr the matrix and store all antennas as a dictionary adding the coords

rows = len(day8input)
cols = len(day8input[0])

m_antinodes_hash = set()
antinodes_hash = set()


def is_inbounds(a):
	return (0 <= a[0] and a[0] < rows) and (0 <= a[1] < cols)

def coord_minus(a):
	dx = a[0]
	dy = a[1]
	return (-dx, -dy)

def coord_sum(a,b):
	dx = a[0] + b[0]
	dy = a[1] + b[1]
	return (dx, dy)

def check_antinode(antinode, antinodes_set=antinodes_hash):
	is_inside = is_inbounds(antinode)
	if is_inside:
		antinodes_set.add(antinode)
	return is_inside

def check_antinodes(ant, diff):
	ant_a = ant

	while is_inbounds(ant_a):

		check_antinode(ant_a, m_antinodes_hash)
		ant_a = coord_sum(ant_a, diff)


def validate_pairs(antennas_coords):
	import itertools
	antennas_pairs = itertools.combinations(antennas_coords, 2)
	total = 0
	for ants_pair in antennas_pairs:
		ants_c = [tuple(map(int, ant_c.split(','))) for ant_c in ants_pair]
		ant_a = ants_c[0]
		ant_b = ants_c[1]
		# 
		diff = coord_sum(ant_a, coord_minus(ant_b))

		# Pt1
		check_antinode(
			coord_sum(ant_a, diff)
		)

		#
		check_antinodes(ant_a, diff)
	
		ant_a = ant_b
		diff = coord_minus(diff)

		# Pt2
		check_antinode(
			coord_sum(ant_a, diff)
		)
		#
		check_antinodes(ant_a, diff)
	


def get_antennas_dict(matrix=day8input):
	antennas_dict = dict()
	for i in range(rows):
		for j in range(cols):
			cell = matrix[i][j]
			if cell != '.':
				# print(cell)
				if cell not in antennas_dict:
					antennas_dict[cell] = []
				cell_index = str(i)+','+str(j)
				antennas_dict[cell].append(cell_index)
	return antennas_dict



if __name__ == '__main__':	
	for a_index, antenna_coords in get_antennas_dict().items():
		print(antenna_coords, a_index)
		# calculate pairs
		validate_pairs(antenna_coords)

	print(len(antinodes_hash))
	assert(len(antinodes_hash) == 252)
	print(len(m_antinodes_hash))
	assert(len(m_antinodes_hash) == 839)
	# 252 and 839
