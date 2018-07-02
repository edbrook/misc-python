#!/usr/bin/env python3

def pivot(array, lo, hi):
    pvt = lo + 1
    for i in range(lo+1, hi):
        if array[i] < array[lo]:
            if i != pvt:
                array[i], array[pvt] = array[pvt], array[i]
            pvt += 1
    sp = pvt - 1
    if lo != sp:
        array[lo], array[sp] = array[sp], array[lo]
    return pvt


def quicksort(array):
    unsorted = [(0, len(array))]
    while unsorted:
        lo, hi = unsorted.pop()
        if lo < hi-1:
            pvt = pivot(array, lo, hi)
            if pvt < hi:
                unsorted.append((pvt, hi))
            if lo < pvt-1:
                unsorted.append((lo, pvt-1))
    return array


if __name__ == '__main__':
    from random import randrange
    # array = [randrange(10,100) for i in range(30)]
    array = [4, 1, 5, 1, 0, 2, 8, 6, 5, 8, 9, 2]
    print(array)
    quicksort(array)
    print(array)
