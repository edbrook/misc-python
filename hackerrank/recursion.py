#!/usr/bin/env python3.6

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n < 1:
        return 0
    elif n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    n = 10
    print(f'fibonacci(n): { [fibonacci(n) for n in range(n)] }')
    print(f'factorial(n): { [factorial(n) for n in range(n)] }')