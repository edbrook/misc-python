#!/usr/bin/env python3

from random import randrange

def shuffle(data):
    n = len(data)
    i = 0
    while i < n:
        j = randrange(i, n)
        data[i], data[j] = data[j], data[i]
        i += 1


if __name__ == '__main__':
    def int_array_to_string(data):
        return ','.join(["{:3d}".format(i) for i in my_array])

    my_array = list(range(-5, 6, 1))
    print("Input array:")
    print(int_array_to_string(my_array))
    print("\nShuffled:")
    for x in range(10):
        shuffle(my_array)
        print(int_array_to_string(my_array))
