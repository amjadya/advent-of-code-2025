def check_valid(lower, upper):
    sum = 0
    for n in range(lower, upper + 1):
        str_n = str(n)
        if len(str_n) % 2 != 0:
            continue
        if str_n[:len(str_n)//2] == str_n[len(str_n)//2:]:
            sum += n
    return sum

if __name__ == "__main__":
    with open("day2/input.txt") as file:
        interval_strings = file.read().strip().split(',')
    
    res = 0
    for s in interval_strings:
        bounds = s.split('-')
        lower = int(bounds[0])
        upper = int(bounds[1])
        res += check_valid(lower, upper)
    
    print(res)