#!/bin/python3

import re


if __name__ == '__main__':
    n, m = [int(n) for n in input().split()]
    
    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    msg = ''.join([matrix[i][j] for j in range(m) for i in range(n)])

    repl = re.compile(r'(?<=[A-Za-z0-9])([^A-Za-z0-9]+)(?=[A-Za-z0-9])')

    print(repl.sub(' ', msg))