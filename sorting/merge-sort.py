#!/usr/bin/env python3

import random
from time import time

class MergeSort:
    @staticmethod
    def sort(data):
        if len(data) < 2:
            return data
        left, right = MergeSort._split(data)
        return MergeSort._merge(
            MergeSort.sort(left),
            MergeSort.sort(right))

    @staticmethod
    def _split(data):
        size = len(data)
        if size <= 1:
            return data
        half = size // 2
        return data[:half], data[half:]
    
    @staticmethod
    def _merge(left, right):
        # print('MERGE:', left, right, end=' => ')
        size_left = len(left)
        size_right = len(right)
        out = []
        l, r = 0, 0
        while l < size_left and r < size_right:
            if left[l] < right[r]:
                out.append(left[l])
                l += 1
            else:
                out.append(right[r])
                r += 1
        out.extend(left[l:])
        out.extend(right[r:])
        # print(out)
        return out


def main():
    min_int = 1
    max_int = 1000
    count = 100000
    nums = [random.randint(min_int, max_int) for _ in range(count)]
    # print(nums)
    before = time()
    # nums.sort()
    nums = MergeSort.sort(nums)
    after = time()
    # print(nums)
    print('Time: {:.5f}s'.format(after - before))


if __name__ == "__main__":
    main()
