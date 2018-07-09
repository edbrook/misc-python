from random import randrange
from time import time


def timeit(fn):
    n = 10
    def wrapper(*args, **kwargs):
        before = time()
        for _ in range(n):
            ans = fn(*args, **kwargs)
        after = time()
        print(f"{n} x {fn.__name__:16s} : {after-before:8.5f}s : {ans}")
        return ans
    return wrapper


@timeit
def min_max(elements):
    return min(elements), max(elements)


@timeit
def for_loop(elements):
    min_ = max_ = elements[0]
    for element in elements:
        if element < min_:
            min_ = element
        elif element > max_:
            max_ = element
    return min_, max_


@timeit
def min_max_elem(elements):
    min_ = max_ = elements[0]
    for element in elements:
        min_ = min(min_, element)
        max_ = max(max_, element)
    return min_, max_


@timeit
def min_max_elem_idx(elements):
    min_ = max_ = elements[0]
    for i in range(len(elements)):
        min_ = min(min_, elements[i])
        max_ = max(max_, elements[i])
    return min_, max_


if __name__ == '__main__':
    elements = [randrange(1e10) for _ in range(1000000)]

    min_max(elements)
    for_loop(elements)
    min_max_elem(elements)
    min_max_elem_idx(elements)