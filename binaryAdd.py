#!/usr/bin/env python3

from sys import argv

'''Quick script to explain the addition of binary numbers'''

def _convert_to_binary_list(s):
    out = []
    for i in range(len(s)):
        value = int(s[i])
        if 0 <= value <= 1:
            out.append(int(s[i]))
        else:
            raise ValueError('Invalid binary number!')
    return out

def add_binary_strings(a,b,debug=False):
    ans = []
    digits = max(len(a),len(b))
    a = _convert_to_binary_list(a.zfill(digits))
    b = _convert_to_binary_list(b.zfill(digits))
    carry = 0
    for i in range(digits-1,-1,-1):
        column_value = a[i] + b[i] + carry
        if column_value == 0:
            value = 0
            carry = 0
        elif column_value == 1:
            value = 1
            carry = 0
        elif column_value == 2:
            value = 0
            carry = 1
        elif column_value == 3:
            value = 1
            carry = 1
        ans.insert(0,value)
        if debug:
            print('a[{0}] = {1}, b[{0}] = {2}, value = {4}, carry = {3}'.format(
                i,a[i],b[i],carry,value))
    if debug:
        print('{:>36s} = {}'.format('carry',carry))
    if carry:
        ans.insert(0,1)
    return ''.join([str(digit) for digit in ans])


if __name__ == '__main__':
    assert isinstance(add_binary_strings('1010','1101'),str), 'Answer must by of type string'
    assert add_binary_strings('1010','1101') == '10111', 'Binary add gave incorrect answer'

    a = argv[1]
    b = argv[2]
    pad = max(len(a),len(b)) + 1
    try:
        ans = add_binary_strings(a,b,True)
        print('    A = {{:>{:d}s}}'.format(pad).format(a))
        print('    B = {{:>{:d}s}}'.format(pad).format(b))
        print('(A+B) = {{:>{:d}s}}'.format(pad).format(ans))
    except ValueError as e:
        print(e)
