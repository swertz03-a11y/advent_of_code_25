def check_neighbors(grid, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    count = 0
    if grid[row][col] == '.':
        return 100
    for dr, dc in directions:
        r, c = row + dr, col + dc
        
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] == '@':
                count += 1
    return count

with open('printingDepartment.txt', 'r') as file:
    grid = []
    for line in file.readlines():
        line = list(line.strip())
        grid.append(line)

running_total = 0
while True:

    total_count = 0 
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            col = row[j]
            if check_neighbors(grid, i, j) < 4:
                total_count += 1  
                grid[i][j] = '.'
    if total_count == 0:
        break
    running_total += total_count
    print("Removing:", total_count)

print("Running total:", running_total)
