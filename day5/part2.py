def merge_intervals(intervals):
    i = 0
    while i < len(intervals) - 1:
        start1, end1 = intervals[i]
        start2, end2 = intervals[i + 1]

        if start2 <= end1:
            intervals[i] = (start1, max(end1, end2))
            del intervals[i + 1]
        else:
            i += 1

if __name__ == "__main__":

    intervals = []
    with open("day5/input.txt") as file:
        # Learning better ways to process information from files
        for line in file:
            line = line.strip()
            if not line:
                continue
            if '-' in line:
                lower, upper = map(int, line.split('-'))
                intervals.append((lower, upper))
    
    # can also just do .sort() or even sorted() but this is better for learning :p
    intervals.sort(key=lambda x: x[0])

    merge_intervals(intervals)

    res = 0
    for interval in intervals:
        res += (interval[1] - interval[0]) + 1

    print(res)