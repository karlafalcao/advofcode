def merge_ranges(ranges):
    # Sort by start of range
    ranges.sort()
    merged = []

    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            # No overlap
            merged.append([start, end])
        else:
            # Overlap → merge
            merged[-1][1] = max(merged[-1][1], end)

    return merged

input = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''
file = open('day5input.txt')
input_r = file.read()
file.close()
input_parts = input_r.split('\n\n')

ranges, ingredients_avail = [input_part.split('\n') for input_part in input_parts]

ranges_splitted = [tuple(map(int, rang.split('-'))) for rang in ranges]

merged_rangs = merge_ranges(ranges_splitted)


print(sum([(b-a)+1 for (a,b) in merged_rangs]))