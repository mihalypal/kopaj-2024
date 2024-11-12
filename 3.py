def parse_string_to_matrix(string):
    matrix = [list(map(int, row.split())) for row in string.strip().split('\n')]
    return matrix

def count_islands(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    visited = set()
    island_count = 0

    def dfs(row, col):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or matrix[row][col] == 0:
            return
        visited.add((row, col))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            dfs(row + dr, col + dc)

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != 0 and (r, c) not in visited:
                dfs(r, c)
                island_count += 1

    return island_count

res = count_islands(parse_string_to_matrix(body))
