def _array_to_str(array):
    return ' '.join([str(i) for i in array])

def _bs_display(array, i):
    l = _array_to_str(array[:i])
    m = _array_to_str(array[i:i+2])
    r = _array_to_str(array[i+2:])
    if len(l) != 0: l = f' {l}'
    if len(r) != 0: r = f'{r} '
    print(f'{l}[{m}]{r}', end='')


def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            _bs_display(array, i)
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
                print(' SWAP', end='')
            print()
        print()


array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# array = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
# array = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]

print(array, end='\n\n')

bubble_sort(array)

print(array)