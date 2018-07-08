def max_hourglass(arr):
    max_total = -63
    for row in range(4):
        for col in range(4):
            top = arr[row]
            mid = arr[row+1]
            bot = arr[row+2]
            total = sum([top[c] for c in range(col, col+3)])
            total += mid[col+1]
            total += sum([bot[c] for c in range(col, col+3)])
            max_total = max(total, max_total)
    return max_total


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(max_hourglass(arr))