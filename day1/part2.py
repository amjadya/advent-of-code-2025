def unlock(starting_position, instruction):
    value = int(instruction[1:])
    direction = instruction[0]
    zeros = value // 100
    
    if direction == 'L':
        end = (starting_position - value) % 100
        if starting_position != 0 and (end > starting_position or end == 0):
            zeros += 1
    else: # 'R'
        end = (starting_position + value) % 100
        if end < starting_position:
            zeros += 1
    return end, zeros

if __name__ == "__main__":
    with open("day1/input.txt") as file:
        input_list = [line.strip() for line in file if line.strip()]
    # print(input_list)

    cur = 50
    res = 0
    for input in input_list:
        cur, zeros = unlock(cur, input)
        res += zeros
    
    print(res)