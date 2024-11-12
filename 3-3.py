def parse_input(input_str):
    # Split the input into rows
    rows = input_str.strip().split("\n")
    
    row_clues = []
    grid = []
    
    for r in rows:
        # Extract row clues (numbers before X's)
        clues_part = ''.join([ch if ch.isdigit() or ch == 'X' else ' ' for ch in r]).strip()
        grid_part = ''.join([ch if ch == 'X' or ch == '□' else ' ' for ch in r]).strip()

        # Extract numbers for clues (split by 'X')
        clues = [int(i) for i in clues_part.split('X') if i]
        
        # Add to row clues
        row_clues.append(clues)
        grid.append(grid_part)
    
    return row_clues, grid

def nonogram_solver(row_clues, grid, size=7):
    # Initialize the grid with empty cells (represented by 0)
    solved_grid = [[0 for _ in range(size)] for _ in range(size)]
    
    # Apply simple logic for filling grid based on row clues
    for r in range(size):
        row_clue = row_clues[r]
        pos = 0
        for length in row_clue:
            # Fill blocks of black squares (1 represents black square)
            for i in range(length):
                solved_grid[r][pos] = 1
                pos += 1
            # Add a white square (0) after each block, except for the last block
            if pos < size and (i + 1 < len(row_clue)):
                solved_grid[r][pos] = 0
                pos += 1

    return solved_grid

def grid_to_output(grid):
    # Convert grid to a readable format
    output = []
    for row in grid:
        output.append(''.join('■' if x == 1 else '□' for x in row))
    return "\n".join(output)

def solve_nonogram(input_str):
    row_clues, grid = parse_input(input_str)
    
    # Solve the puzzle
    solved_grid = nonogram_solver(row_clues, grid)
    
    # Convert grid to output format
    return grid_to_output(solved_grid)

# Test the function with the example input
input_str = """
XXX11512
XXX1XXX1
XXXXXXXX
111□□□□□
11X□□□□□
4XX□□□□□
11X□□□□□
1XX□□□□□
"""

output_str = solve_nonogram(input_str)
print(output_str)
