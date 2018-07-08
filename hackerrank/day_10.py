def consecutive_ones(num):
    max_ones = ones = 0
    while num > 0:
        if num & 1:
            ones += 1
        else:
            max_ones = max(max_ones, ones)
            ones = 0
        num >>= 1
    return max(max_ones, ones)


if __name__ == '__main__':
    n = int(input())
    print(consecutive_ones(n))