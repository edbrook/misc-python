from collections import deque

def merge_sort(array, _depth=0):
    if len(array) == 1:
        return list(array)
    padding = f'{"|----" * _depth}> '
    split = len(array) // 2
    left = array[:split]
    right = array[split:]
    print(f'{padding}SPLIT : {array} --> {left}, {right}')
    left = merge_sort(left, _depth+1)
    right = merge_sort(right, _depth+1)
    result = []
    print(f'{padding}MERGE : {left}, {right}', end='')
    l, l_len = 0, len(left)
    r, r_len = 0, len(right)
    while l < l_len and r < r_len:
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result.extend(left[l:])
    result.extend(right[r:])
    print(f' --> {result}', end='\n\n' if _depth == 0 else '\n')
    return result


array = [26, 54, 93, 17, 77, 31, 44, 55, 20]

print(array, end='\n\n')

array = merge_sort(array)

print(array)
