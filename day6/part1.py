def solve_problem(j, rows):
    operation = rows[-1][j]
    sum = 0
    prod = 1
    if operation == '+':
        for i in range(len(rows) - 1):
            sum += int(rows[i][j])
        # print(sum)
        return sum
    else: # '*'
        for i in range(len(rows) - 1):
            prod *= int(rows[i][j])
        # print(prod)
        return prod

if __name__ == "__main__":
    with open("day6/input.txt") as file:
        rows = []
        for line in file:
            nums = line.split()
            rows.append(nums)
            # print(nums)

    res = 0
    for j in range(len(rows[0])):
        res += solve_problem(j, rows)
    
    print(res)