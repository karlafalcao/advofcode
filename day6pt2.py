def parse_grid(grid):
    """
    Parses the grid to find the guard's starting position and direction.
    """
    direction_map = {
        '^': 0,  # up
        '>': 1,  # right
        'v': 2,  # down
        '<': 3,  # left
    }

    nrows = len(grid)
    ncols = len(grid[0])

    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] in direction_map:
                return r, c, direction_map[grid[r][c]]

    raise ValueError("No starting position found in the grid.")

def move_guard(grid):
    """
    Simulates the guard's movement and returns the set of visited positions.
    """
    start_row, start_col, direction_index = parse_grid(grid)
    nrows = len(grid)
    ncols = len(grid[0])

    # Directions in the order: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    row, col = start_row, start_col
    d = direction_index

    visited = set([(row, col)])

    while True:
        # Compute the cell in front of the guard
        dr, dc = directions[d]
        front_row = row + dr
        front_col = col + dc

        # Check if front cell is blocked or out-of-bounds
        if (front_row >= 0 and front_row < nrows and
            front_col >= 0 and front_col < ncols and
            grid[front_row][front_col] == '#'):
            # Turn right
            d = (d + 1) % 4
        else:
            # Move forward
            row, col = front_row, front_col

            # If the guard has stepped out of the map, break
            if row < 0 or row >= nrows or col < 0 or col >= ncols:
                break

            visited.add((row, col))

    return visited

def solve_guard_patrol(grid):
    """
    Given a list of strings representing the map,
    returns the number of distinct positions the guard visits.
    """
    
    visited = move_guard(grid)
    return len(visited)

def has_loop(grid):
    """
    Determines if the guard's patrol results in a loop.
    Returns True if a loop is detected, False otherwise.
    """
    start_row, start_col, direction_index = parse_grid(grid)
    nrows = len(grid)
    ncols = len(grid[0])

    # Directions in the order: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    row, col = start_row, start_col
    d = direction_index

    path_block_history = {}

    while True:

        # Compute the cell in front of the guard
        dr, dc = directions[d]
        front_row = row + dr
        front_col = col + dc

        # Check if front cell is blocked or out-of-bounds
        if (front_row >= 0 and front_row < nrows and
            front_col >= 0 and front_col < ncols and
          (  grid[front_row][front_col] == '#' or grid[front_row][front_col] == 'O')):
            # Turn right
            d = (d + 1) % 4

            # Track path for loop detection
            hash_key = ",".join([str(front_row), str(front_col),str(d)])
            # print(hash_key)
            # add in a dict
           
            if hash_key in path_block_history:
                # Detected a loop
                return True
            path_block_history[hash_key] = 1
        else:
            # Move forward
            row, col = front_row, front_col

            # If the guard has stepped out of the map, return False
            if row < 0 or row >= nrows or col < 0 or col >= ncols:
                return False

       
    return False

def count_looped(mazes_list, expected=None):
    from collections import Counter
    count = Counter([has_loop(maze) for maze in mazes_list]).most_common()
    print(count)

    if expected:
        assert(count == expected)

    return dict(count)[True]

if __name__ == "__main__":

    # Example puzzle input (10 lines, each 10 chars wide):
    puzzle_input = [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#...",
    ]
    # from day6input import puzzle_input

    result = solve_guard_patrol(puzzle_input)
    print("Number of distinct positions visited:", result)

    # loop detector
    from day6input import example_all, example_looped
    
    loop_detected = has_loop(example_looped[0])
    print("Does the guard's patrol have a loop?:", loop_detected)

    looped_mazes = count_looped(example_looped)
    print("Number of loopedmazes:", looped_mazes)
    looped_mazes = count_looped(example_all)
    print("Number of loopedmazes:", looped_mazes)
    
    # Test against real input
    from day6input import day6input
    result = solve_guard_patrol(day6input)
    print("Number of distinct positions visited:", result)

    import os
    os.system('deno --allow-read --allow-write day6pt2.ts')
    #
    # TODO: run day6pt2.ts to generate day6input_mazes variable
    from day6input_mazes import day6input_mazes

    looped_mazes = count_looped(day6input_mazes, expected=[(False, 3312), (True, 1957)])
    print("Number of loopedmazes:", looped_mazes)
    # delete file day6input_mazes.py
    delete_file = ''
    while delete_file != 'y' and delete_file != 'n':
        delete_file = input("Should delete day6input_mazes.py file(y/n)?")
        print(delete_file)

        if delete_file == 'y':
            os.remove('day6input_mazes.py')
    
