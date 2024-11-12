def parse_string_to_matrix(string):
    string = string.replace('\\n', '\n')
    strlist = string.split('\n')
    return strlist

def count_islands(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    visited = set()
    island_count = 0

    def dfs(row, col):
        # Check if the cell is already visited or out of bounds or is water ('0')
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or matrix[row][col] == '0':
            return
        visited.add((row, col))

        # Explore all 4 possible directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            dfs(row + dr, col + dc)

    # Traverse each cell in the matrix
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '1' and (r, c) not in visited:
                # Found an unvisited land cell, start a DFS from here
                dfs(r, c)
                island_count += 1

    return island_count

# Test input
matrix_string = '11101001\n11011011\n00100011\n11111111\n11111000\n11011101\n10011101\n11110110\n11111011\n01100011'
matrix = parse_string_to_matrix(matrix_string)

# Print matrix rows for debugging
for row in matrix:
    print(''.join(row))

# Count and print the number of islands
res = count_islands(matrix)
print("Number of islands:", res)