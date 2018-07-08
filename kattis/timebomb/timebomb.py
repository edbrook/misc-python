#!/usr/bin/env python3

ascii_code = [
    {'***':[0,2,3,5,6,7,8,9], '  *':[1,], '* *':[4,]}, # ***   * *** *** * * *** *** *** *** ***
    {'* *':[0,4,8,9], '  *':[1,2,3,7], '*  ':[5,6]},   # * *   *   *   * * * *   *     * * * * *
    {'* *':[0,], '  *':[1,7], '***':[2,3,4,5,6,8,9]},  # * *   * *** *** *** *** ***   * *** *** 
    {'* *':[0,6,8], '  *':[1,3,4,5,7,9], '*  ':[2,]},  # * *   * *     *   *   * * *   * * *   * 
    {'***':[0,2,3,5,6,8,9], '  *':[1,4,7]},            # ***   * *** ***   * *** ***   * *** *** 
]

rows = 5
width = 3
code_len = -1
possible_digits = []
msg = None
for row in range(rows):
    line = input()
    if msg:
        break
    number_segments = [line[x:x+width+1][:width] for x in range(0, len(line), width+1)]
    for i in range(len(number_segments)):
        segment = number_segments[i]
        if segment in ascii_code[row]:
            matching_digits = ascii_code[row][segment]
            if row == 0:
                possible_digits.append(matching_digits)
            else:
                possible_digits[i] = [digit for digit in matching_digits if digit in possible_digits[i]]
                if len(possible_digits[i]) == 0:
                    msg = 'BOOM!!'
        else:
            msg = 'BOOM!!'

if msg:
    print(msg)
else:
    code = int(''.join([str(digits[0]) for digits in possible_digits]))
    print((code % 6 == 0) and 'BEER!!' or "BOOM!!")
