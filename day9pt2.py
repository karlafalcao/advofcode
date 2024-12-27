def parse_map_to_blocks(disk_map_str):
    """
    Parse the dense format (digits alternate between file length and free length)
    into a list of blocks, where each block is either:
      - an integer file ID, or
      - '.' representing free space.
    """
    blocks = []
    file_id = 0
    i = 0
    n = len(disk_map_str)

    while i < n:
        # 1) file length
        file_len = int(disk_map_str[i])
        i += 1
        
        # Add 'file_len' blocks for this file
        for _ in range(file_len):
            blocks.append(file_id)
        file_id += 1

        # 2) free length (if another digit remains)
        if i < n:
            free_len = int(disk_map_str[i])
            i += 1
            
            for _ in range(free_len):
                blocks.append('.')

    return blocks


def build_file_spans(blocks):
    """
    Build a dictionary mapping fileID -> (start_index, end_index, length).
    This will help us know where each file currently resides in `blocks`.
    """
    file_spans = {}  # fileID -> (start, end, length)

    for idx, block in enumerate(blocks):
        if block != '.':
            f_id = block
            if f_id not in file_spans:
                # First block of this file
                file_spans[f_id] = [idx, idx]  # store start and end
            else:
                # Update the end index
                file_spans[f_id][1] = idx

    # Convert each [start, end] -> (start, end, length)
    for f_id, (start, end) in file_spans.items():
        length = end - start + 1
        file_spans[f_id] = (start, end, length)

    return file_spans


def find_leftmost_free_span(blocks, file_len, file_start):
    """
    Find the leftmost span of length `file_len` consisting of '.' 
    that lies entirely to the left of `file_start`.
    If found, return the starting index of that free span. Otherwise, return None.
    """
    # The free span must end before 'file_start', so the latest possible
    # start index is (file_start - file_len).
    max_start_index = file_start - file_len
    if max_start_index < 0:
        return None

    i = 0
    while i <= max_start_index:
        # Check if blocks[i..i+file_len-1] are all '.'
        all_dots = True
        for j in range(file_len):
            if blocks[i + j] != '.':
                all_dots = False
                break

        if all_dots:
            return i
        else:
            i += 1

    return None


def move_file(blocks, old_start, old_end, new_start):
    """
    Move an entire file (currently occupying [old_start..old_end]) 
    into the free space beginning at new_start (length = old_end - old_start + 1).
    """
    file_id = blocks[old_start]
    file_len = (old_end - old_start + 1)

    # 1) Wipe out the old region
    for pos in range(old_start, old_end + 1):
        blocks[pos] = '.'

    # 2) Fill the new region with file_id
    for offset in range(file_len):
        blocks[new_start + offset] = file_id


def compact_whole_files(blocks):
    """
    Move each file at most once in descending file ID order.
    If there's a contiguous free region to the left that can fit the file, move it;
    otherwise, leave it in place.
    """
    file_spans = build_file_spans(blocks)
    if not file_spans:
        return blocks  # no files at all

    max_file_id = max(file_spans.keys())

    # Iterate from highest file ID down to 0
    for f_id in range(max_file_id, -1, -1):
        if f_id not in file_spans:
            continue  # skip files that don't exist

        (start, end, length) = file_spans[f_id]

        # Find the leftmost free span to the left of 'start' that can fit 'length'
        free_start = find_leftmost_free_span(blocks, length, start)
        if free_start is not None:
            # Move the file in one shot
            move_file(blocks, start, end, free_start)

            # Update the file's new span in file_spans
            new_start = free_start
            new_end = free_start + length - 1
            file_spans[f_id] = (new_start, new_end, length)

    return blocks


def compute_checksum(blocks):
    """
    Sum of (index * fileID) for all file blocks (ignoring free space).
    """
    total = 0
    for idx, val in enumerate(blocks):
        if val != '.':
            # 'val' is the file ID
            total += idx * val
    return total


def solve_whole_file_compaction(disk_map_str):
    """
    Main routine for part 2:
     1) Parse the input disk map
     2) Compact by moving whole files in descending ID order
     3) Compute and return the checksum
    """
    import json
    # 1) Parse
    blocks = parse_map_to_blocks(disk_map_str)
    # print(blocks)
    with open('outputday9rawblocks.txt', 'w') as file:
        json.dump(blocks, file, indent=0)

  
    # 2) Perform whole-file compaction
    blocks = compact_whole_files(blocks)
    with open('outputday9pt2gpt.txt', 'w') as file:
        json.dump(blocks, file, indent=0)

  
    # 3) Compute checksum
    return compute_checksum(blocks)


# ---------------------------------------------------------------------
# Example usage (with a smaller example from the puzzle statement):
if __name__ == "__main__":
    # This "first example" in the puzzle text might be:
    # "2333133121414131402" (the same example as part 1, but the moves differ).
    # The puzzle’s text for part 2 says the final checksum in the example is 2858.
    file = open('./day9input.txt', 'r')
    file_content = file.read()
    file.close()


    example_input = file_content
    # example_input = "2333133121414131402"
    result = solve_whole_file_compaction(example_input)
    print(f"Checksum for example = {result}")
    # Expected (according to puzzle statement): 2858
