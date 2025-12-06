def check_joltage(batteries):
    # print(batteries)
    max1 = -1
    max2 = -1
    for i, num_s in enumerate(batteries): # Go thru each character in the string (they're just numbers)
        num = int(num_s)
        if num > max1:
            if i == len(batteries) - 1: # Special case if you found the biggest number at the last index
                return (max1, num)
            max1 = num
            max2 = -1
            continue
        if num > max2:
            max2 = num
    return (max1, max2)

if __name__ == "__main__":
    with open("day3/input.txt") as file:
        input_list = [line.strip() for line in file if line.strip()]

    res = 0
    for input in input_list:
        batteries = check_joltage(input)
        # print(batteries)
        res += batteries[0]*10 + batteries[1]

    print(res)