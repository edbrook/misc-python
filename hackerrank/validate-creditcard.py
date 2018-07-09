import re

cc_number = re.compile(r'(?!.*?(\d)(?:-?\1){3}.*)[456]\d{3}(-?\d{4}){3}$')


n = int(input())
for _ in range(n):
    num = input()
    print('Valid' if cc_number.match(num) else 'Invalid')

'''
► It must start with a 4, 5 or 6. 
► It must contain exactly 16 digits. 
► It must only consist of digits (0-9). 
► It may have digits in groups of 4, separated by one hyphen "-". 
► It must NOT use any other separator like ' ' , '_', etc. 
► It must NOT have 4 or more consecutive repeated digits.

Example

Input:
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Output:
Valid
Valid
Invalid
Valid
Invalid
Invalid


// Extension - if you need to have more than one set of repeated digits
print('OK?',bool(
    re.match(
        r'(?!(?:.*?(\d)(?:-?\1){3}){3}.*)',
        '5133-3368-8880-1111')))
'''