import re
from collections import defaultdict

def solve_problem(j, rows):
    m = defaultdict(list)
    operation = rows[-1][j]
    sum = 0
    prod = 1
    # get the list of numbers for that column
    for i in range(len(rows) - 1):
        for k in range(len(rows[i][j])): # go through the string indices
            if rows[i][j][k] != ' ':
                m[k].append(rows[i][j][k])
    if operation == '+':
        for k, v in m.items():
            number = 0
            exponent = len(v)
            for cur_v in v:
                exponent -= 1
                number += int(cur_v) * 10**(exponent)
            sum += number
        return sum
    else: # '*'
        for k, v in m.items():
            number = 0
            exponent = len(v)
            for cur_v in v:
                exponent -= 1
                number += int(cur_v) * 10**(exponent)
            prod *= number
        return prod

if __name__ == "__main__":
    with open("day6/input.txt") as file:
        rows = []
        col_widths = []
        prev_line = next(file) # we want to stop a line early so:
        for line in file:
            arr = prev_line.strip().split()
            for i, num in enumerate(arr):
                if i >= len(col_widths):
                    col_widths.append(len(num))
                else:
                    col_widths[i] = max(col_widths[i], len(num))
            prev_line = line # this is going to let us process everything up till the last line

        file.seek(0) 
        # you only really want to do streaming if the input is on order of GBs, 
        # it's probably better to just do lines = file.read().splitlines() and then work off memory
        # I'm doing this for learning so it's ok
        prev_line = next(file)
        for line in file:
            # take col_widths[i] characters from line, skip one space, take col_widths[i+1] characters from line, skip one space... combine into one array
            row = []
            i = 0
            for width in col_widths:
                row.append(prev_line[i : i + width])
                i += width + 1
            rows.append(row)
            prev_line = line
    rows.append(prev_line.split()) # get the operator line
    
    res = 0
    for j in range(len(rows[0])):
        res += solve_problem(j, rows)
    
    print(res)