def unlock(starting_position, instruction):
    value = int(instruction[1:])
    direction = instruction[0]
    if direction == 'L':
        end = (starting_position - value) % 100
    else: # 'R'
        end = (starting_position + value) % 100
    return end

if __name__ == "__main__":
    with open("day1/input.txt") as file:
        input_list = [line.strip() for line in file if line.strip()]
    # print(input_list)

    cur = 50
    res = 0
    for input in input_list:
        cur = unlock(cur, input)
        if cur == 0:
            res += 1
    
    print(res)