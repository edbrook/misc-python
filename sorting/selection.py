def _array_to_str(array):
    return ''.join([f'{str(i):^4s}' for i in array])


def _ss_display(array, left, right):
    l  = _array_to_str(array[:left])
    sl = array[left]
    m  = _array_to_str(array[left+1:right])
    sr = array[right]
    r  = _array_to_str(array[right+1:])
    print(f'{l}[{sl}]{m}[{sr}]{r} SWAP')


def selection_sort(array):
    for right in range(len(array)-1, 0, -1):
        idx_of_max = right
        for left in range(right):
            if array[left] > array[idx_of_max]:
                idx_of_max = left
        if idx_of_max != right:
            _ss_display(array, idx_of_max, right)
            array[idx_of_max], array[right] = array[right], array[idx_of_max]
    print()


array = [26, 54, 93, 17, 77, 31, 44, 55, 20]

print(array, end='\n\n')

selection_sort(array)

print(array)