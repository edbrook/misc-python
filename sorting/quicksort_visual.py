#!/usr/bin/env python3

from termcolor import colored as c


class Quicksort:
    @staticmethod
    def _print_val(args, kwargs):
        print(c(*args, **kwargs), end=' ')

    @staticmethod
    def _display(array, i, pvt, lo, hi, msg):
        '''Quick & dirty way of visualising the quicksort operations'''
        msg_colour = {'NXT': 'white', 'SWP': 'cyan', 'PVT': 'red'}
        print(c(''.join((msg,': ')), msg_colour[msg], attrs=['bold']), end='')
        for j in range(len(array)):
            val = '{:>2s}'.format(str(array[j]))
            args = [val]
            kwargs = {}
            if j == pvt:
                args.append('yellow')
                kwargs['attrs'] = ['bold']
                if msg == 'PVT':
                    args.append('on_green')
                elif msg == 'SWP':
                    args.append('on_cyan')
                elif j == hi - 1:
                    args.append('on_red')
                    kwargs['attrs'].append('reverse')
            elif j == lo:
                args.append('green')
                if msg == 'PVT':
                    args.append('on_yellow')
            elif j == hi - 1:
                args.append('red')
            elif j > lo and j < hi:
                args.append('blue')
            else:
                args.append('white')
                kwargs['attrs'] = ['dark']
            if i == j and j != pvt and msg != 'PVT' and len(args) < 3:
                if msg == 'SWP':
                    args.append('on_yellow')
                else:
                    args.append('on_cyan')
            Quicksort._print_val(args, kwargs)
        print()

    @staticmethod
    def _pivot(array, lo, hi):
        pvt = lo + 1
        for i in range(lo+1, hi):
            if not (array[i] < array[lo] and i != pvt):
                Quicksort._display(array, i, pvt, lo, hi, 'NXT')
            if array[i] < array[lo]:
                if i != pvt:
                    Quicksort._display(array, i, pvt, lo, hi, 'SWP')
                    array[i], array[pvt] = array[pvt], array[i]
                pvt += 1
        sp = pvt - 1
        if lo != sp:
            Quicksort._display(array, i, pvt-1, lo, hi, 'PVT')
            array[lo], array[sp] = array[sp], array[lo]
        return pvt

    @staticmethod
    def quicksort(array):
        unsorted = [(0, len(array))]
        while unsorted:
            lo, hi = unsorted.pop()
            if lo < hi-1:
                pvt = Quicksort._pivot(array, lo, hi)
                if pvt < hi:
                    unsorted.append((pvt, hi))
                if lo < pvt - 1:
                    unsorted.append((lo, pvt - 1))


if __name__ == '__main__':
    from random import randrange
    array = [randrange(100) for i in range(15)]
    print(array)
    Quicksort.quicksort(array)
    print(array)