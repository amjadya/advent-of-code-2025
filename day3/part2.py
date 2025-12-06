def check_joltage(batteries):
    len_batteries = len(batteries)
    monotonic_stack = []
    monotonic_stack.append(-1)
    for i, num_s in enumerate(batteries):
        num = int(num_s)
        # Stack exists, monotonic condition and you have enough batteries left to ensure min length of 12 in stack 
        while monotonic_stack and monotonic_stack[-1] < num and (len_batteries - i) > 12 - len(monotonic_stack):
            monotonic_stack.pop()
        monotonic_stack.append(num)
    
    # Now we have to pop the last few parts of the stack in case there's extra
    while len(monotonic_stack) != 12:
        monotonic_stack.pop()

    # And add the right weights together
    full_number = 0
    for k in range(12):
        full_number += monotonic_stack.pop()*10**k
    return full_number

if __name__ == "__main__":
    with open("day3/input.txt") as file:
        input_list = [line.strip() for line in file if line.strip()]

    res = 0
    for input in input_list:
        res += check_joltage(input)
    print(res)