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

    if index_toggle and count:
        index += 1
    index_toggle = not index_toggle

    return destructured_list

# print(count_string)
blocks = []
for count in list(count_string):
    
    destruct_list = check_current_count(int(count))
    # print(destruct_list)
    # create a list for 
    # blocks.append(destruct_list)
    blocks += destruct_list

def check_block_from(i, j):
    # 
    # print("Is equal", i, j, )
    i_c = i + 1 
    j_c = j - 1

    # while is blank move i
    # while is the same blocks[j] move the j
    #  get file block
    while (blocks[j_c] == blocks[j_c + 1]):
        j_c -= 1
    
    number_interval = (j_c+1, j+1)
    number_interval_size = number_interval[1] - number_interval[0]
    # print(
    #   "number_interval",
    #   number_interval, 
    #   number_interval_size,
    #   [blocks[i] for i in range(*number_interval)] 
    # )

    # look for a empty space
    # if found then copy
    while (blocks[i_c] == blocks[i_c - 1]):
        i_c += 1

    empty_interval = (i, i_c)
    empty_interval_size = empty_interval[1] - empty_interval[0] 
    # print(
    #   "empty_interval",
    #   empty_interval, 
    #   empty_interval_size,
    #   [blocks[i] for i in range(*empty_interval)] 
    # )

    # MISSING case 
    if i_c >= j_c+1:
        # empty space not found anywhere return reset left pointer 0,j_c
        # return next index to the left
        # print("i_c,j_c", i_c, j_c, blocks[j_c])
        return (0, j_c)

    if number_interval_size <= empty_interval_size:
        # if match do replacement
        # if found replace the empty
        number_interval_range = range(*number_interval)
        empty_interval_range =  range(*empty_interval)
        for (n, e) in zip(number_interval_range, empty_interval_range):
            # print(n, e, [blocks[n], blocks[e]])
            # set leftmost empty index
            [blocks[n], blocks[e]] = [blocks[e], blocks[n]]
        # print(blocks)
        return (0, j)

    # empty space not found look for nextempy space
    # print(i_c, j)
    # subtract the space
    return (i_c, j)

i = 0
j = len(blocks) - 1
# print(i, j)
# print(blocks)
while (0 <= j):
    if blocks[i] == '.' and blocks[j] != '.':
        (i,j) = check_block_from(i, j)
        # continue
    # print(i, j)
    # if (i > j):
    #     break

    if blocks[i] != '.':
        i +=1

    if blocks[j] == '.':
        j -=1
    

# 
# print(i, j)


checksum = 0
for idx, value in enumerate(blocks):
    if value == '.': continue
    blocks[idx] = int(value)
    checksum += idx * int(value)
print(blocks)

print(checksum)
