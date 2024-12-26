

day23input = [line.strip().split('-') for line in open('day23example.txt')]
# day23input = [line.strip().split('-') for line in open('day23input.txt')]

# print(day23input)

conns = dict()
def get_conns():
	for x, y in day23input:
		if x not in conns: conns[x] = set() 
		if y not in conns: conns[y] = set() 

		conns[x].add(y)
		conns[y].add(x)

closed_set = set()

def search(node, frontier):
	closed_set_key = tuple(sorted(frontier))
	if closed_set_key in closed_set: return
	closed_set.add(closed_set_key)
	for neighbor in conns[node]:
		if neighbor in frontier: continue
		# if its a child of every frontier item
		if all(neighbor in conns[front] for front in frontier):
			# insert neighbor
			search(neighbor, {*frontier, neighbor})


get_conns()
# print(conns)

for x in conns:
	search(x, {x})
	
print(closed_set, len(closed_set))
print(','.join(max(closed_set, key=len)))
# print('Triangles')
# print(triangles)

# print(len([triangle for triangle in triangles if any(tri.startswith('t') for tri in triangle)]))


