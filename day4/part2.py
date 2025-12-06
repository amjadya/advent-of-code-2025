def rolls_accessed(grid):
    res = 0
    length = len(grid)
    width = len(grid[0])
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
    for r in range(length):
        for c in range(width):
            sum = 0
            for d in dirs:
                nr, nc = d[0] + r, d[1] + c
                if nr >= 0 and nc >= 0 and nr < length and nc < width:
                    sum += grid[nr][nc]
            if sum < 4 and grid[r][c] == 1:
                res += 1
                grid[r][c] = 0
    return res

if __name__ == "__main__":
    with open("day4/input.txt") as file:
        input_list = [line.strip() for line in file if line.strip()]
    grid = []
    for input in input_list:
        grid_row = []
        for i in range(len(input)):
            if input[i] == '.':
                grid_row.append(0)
            else: # '@'
                grid_row.append(1)
        grid.append(grid_row)
    
    # for line in grid:
    #     print(line)
    multi_res = 0
    res = -1
    while res != 0:
        res = rolls_accessed(grid)
        multi_res += res

    print(multi_res)