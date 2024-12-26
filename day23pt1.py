

day23input = [line.strip().split('-') for line in open('day23example.txt')]
day23input = [line.strip().split('-') for line in open('day23input.txt')]

print(day23input)


conns = dict()

for x, y in day23input:
	print(x, y)
	if x not in conns: conns[x] = set() 
	if y not in conns: conns[y] = set() 

	conns[x].add(y)
	conns[y].add(x)


triangles = set()
for x in conns:
	for y in conns[x]:
		for z in conns[y]:
			if x != z and x in conns[z]:
				triangles.add(tuple(sorted([x,y,z])))


print(conns)
print('Triangles')
print(triangles)

print(len([triangle for triangle in triangles if any(tri.startswith('t') for tri in triangle)]))


	