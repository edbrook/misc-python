import re

and_or_re = re.compile(r'(?<= )(?<!\||&)(\|\||&&)(?= )')

def and_or(match):
    op = match.groups()[0]
    if op == '||': return 'or'
    if op == '&&': return 'and'

n = int(input())
for _ in range(n):
    line = input()
    print(and_or_re.sub(and_or, line))