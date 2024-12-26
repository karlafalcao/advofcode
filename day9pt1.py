from day9input import day9input

index = 0
empty_char = '.'
index_toggle = True
count_string = day9input

def check_current_count(count):
	global index_toggle
	global index
	destructured_list = []

	for i in range(0, count):
		if index_toggle:
			destructured_list.append(str(index))
			# print(str(index))
		else:
			destructured_list.append(empty_char)
			# print(empty_char)

	if index_toggle:
		index += 1
	index_toggle = not index_toggle

	return destructured_list

print(count_string)
destructured_all = []
for count in list(count_string):
	
	destruct_list = check_current_count(int(count))
	print(destruct_list)
	destructured_all += destruct_list

i = 0
j = len(destructured_all) - 1

while (j > i ):
	# 
	# print(destructured_all[i])
	# print(destructured_all[j])
	if destructured_all[i] == '.' and destructured_all[j] != '.':
		[destructured_all[i], destructured_all[j]] = [destructured_all[j], destructured_all[i]]

	if destructured_all[i] != '.':
		i +=1

	if destructured_all[j] == '.':
		j -=1

# 
# print(i, j)
# print(destructured_all)

checksum = 0
for dest_i in range(len(destructured_all)):
	if destructured_all[dest_i] == '.': break
	checksum += int(destructured_all[dest_i]) * dest_i
print(checksum)