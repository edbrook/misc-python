#!/usr/bin/env python3

def pivot(array, lo, hi):
    pvt = lo + 1
    print("Pvt:%d, Lo:%d, Hi:%d" % (pvt, lo, hi-1))
    for i in range(lo+1, hi):
        # print(array[i], array[lo], pvt)
        if array[i] < array[lo]:
            if i != pvt:
                print("SWP arr[%d](%d) <--> arr[%d](%d)" % (pvt, array[pvt], i, array[i]))
                array[i], array[pvt] = array[pvt], array[i]
            pvt += 1
    sp = pvt - 1
    if lo != sp:
        print("PVT arr[%d](%d) <--> arr[%d](%d)" % (lo, array[lo], sp, array[sp]))
        array[lo], array[sp] = array[sp], array[lo]
    print("ARR: %s" % array)
    return pvt


def quicksort(array):
    print("ARR: %s" % array)
    unsorted = [(0, len(array))]
    while unsorted:
        lo, hi = unsorted.pop()
        if lo < hi-1:
            pvt = pivot(array, lo, hi)
            if pvt < hi:
                unsorted.append((pvt, hi))
            if lo < pvt-1:
                unsorted.append((lo, pvt-1))


if __name__ == '__main__':
    from random import randrange
    # quicksort([randrange(10,100) for i in range(30)])
    quicksort([4, 1, 5, 1, 0, 2, 8, 6, 5, 8, 9, 2])
