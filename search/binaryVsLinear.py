#!/usr/bin/env python3

from random import randrange

def linear_search(array, target):
    c = 0   # only used to count comparisons
    for i in range(len(array)):
        c += 1
        # print(array[i], i)
        if array[i] == target:
            return i, c
    return None, c


def binary_search(array, target):
    c = 0   # only used to count comparisons
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        c += 1
        i = lo + (hi - lo) // 2
        val = array[i]
        # print(val, i, lo, hi)
        if val == target:
            return i, c
        elif val < target:
            lo = i + 1
        elif val > target:
            hi = i - 1
    return None, c


def main():
    size = randrange(10, 50000)
    array = [randrange(1e7) for _ in range(size)]
    array.sort()
    index = randrange(size)
    target = array[index]

    # print('Array:', array)
    print('Array Size:', size)
    print('Target:', target)
    
    ls_idx, ls_steps = linear_search(array, target)
    bs_idx, bs_steps = binary_search(array, target)

    print('Index - Expected: {}, Linear: {}, Binary: {}'.format(index, ls_idx, bs_idx))
    print('Num steps for - Linear: {}, Binary: {}'.format(ls_steps, bs_steps))

if __name__ == '__main__':
    main()