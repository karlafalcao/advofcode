from day9input import day9input, day9input_example
import json

# TODO: improve performance if keep the first_empty space pivot

index = 0
index_toggle = True

def check_current_size(b_size):
    global index_toggle
    global index
    destructured_list = []

    for i in range(0, b_size):
        if index_toggle:
            destructured_list.append(index)
        else:
            destructured_list.append('.')

    if index_toggle and b_size:
        index += 1
    index_toggle = not index_toggle

    return destructured_list

# print(count_string)

def build_blocks(blocks, blocks_sizes):
    for b_size in list(blocks_sizes):
        destruct_list = check_current_size(int(b_size))
        # sumup the list for all blocks
        blocks += destruct_list

def move_file(blocks, file_interval, empty_interval):
    """
    Move an entire file (currently occupying [...file_interval...]) 
    into the free space located in [...empty_interval]
    """
    #  Swap the old(blank) space with the file id
    for (n, e) in zip(range(*file_interval), range(*empty_interval)):
        [blocks[n], blocks[e]] = [blocks[e], blocks[n]]

def get_empty_interval(blocks, i):
    # read_block_span
    i_c = i + 1
    while (blocks[i_c] == '.' and blocks[i_c] == blocks[i_c - 1]):
        i_c += 1
    empty_interval = (i, i_c)
    empty_interval_size = empty_interval[1] - empty_interval[0]
    return empty_interval, empty_interval_size


def get_file_interval(blocks, j):
    # 
    j_c = j - 1
    while (blocks[j_c] == blocks[j_c + 1]):
        j_c -= 1
    file_interval = (j_c+1, j+1)
    file_interval_size = file_interval[1] - file_interval[0]
    return file_interval, file_interval_size


def check_block_from(blocks, i, j):

    file_interval, file_interval_size = get_file_interval(blocks, j)
    (j_c, jplus) = file_interval
    # read_block_span
    empty_interval, empty_interval_size = get_empty_interval(blocks, i)
    (i, i_c) = empty_interval

    if i_c >= j_c:
        # skip case
        if blocks[i_c] == blocks[j_c+1] and empty_interval_size == file_interval_size:
            print('CONFLICT: i_c=', i_c, 'j_c= ', j_c, blocks[i_c], blocks[j_c+1])
            print("check_block_from", i,j)
            print('empty_interval_size i=',i, 'i_c-1=',i_c-1, blocks[i], blocks[i_c-1], empty_interval_size)
            print('file_interval_size j_c+1=', j_c+1, 'j= ', j, blocks[j_c+1], blocks[j], file_interval_size)
        else:
            return (0, j_c-1)

    if file_interval_size <= empty_interval_size:
        move_file(blocks, file_interval, empty_interval)
        return (0, j_c)

    return (i_c, j)


def compact_blocks(blocks):
    i = 0
    j = len(blocks) - 1

    while (0 <= j and i <= len(blocks) - 1):
        if blocks[i] == '.' and blocks[j] != '.':
            (i,j) = check_block_from(blocks, i, j)
        if blocks[i] != '.':
            i +=1
        if blocks[j] == '.':
            j -=1
    

def calc_checksum():
    checksum = 0
    for idx, value in enumerate(blocks):
        if value == '.': continue
        blocks[idx] = int(value)
        checksum += idx * int(value)

    return checksum

blocks = []
blocks_sizes = day9input_example
blocks_sizes = day9input
build_blocks(blocks, blocks_sizes)
with open('outputday9rawblocks.txt', 'w') as file:
    json.dump(blocks, file, indent=0)

compact_blocks(blocks)
with open('outputday9pt2.txt', 'w') as file:
    json.dump(blocks, file, indent=0)

print("Your puzzle answer is", calc_checksum())

