if __name__ == "__main__":

    interval_strings = []
    id_strings = []
    with open("day5/input.txt") as file:
        input_list = [line.strip() for line in file if line.strip()]
    
    for input in input_list:
        if '-' in input:
            interval_strings.append(input)
        else:
            id_strings.append(input)
    
    res = 0
    for s in interval_strings:
        bounds = s.split('-')
        lower = int(bounds[0])
        upper = int(bounds[1])
        
        for id in id_strings[:]:
            if lower <= int(id) <= upper:
                res+=1
                id_strings.remove(id)
    print(res)