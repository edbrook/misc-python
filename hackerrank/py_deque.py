from collections import deque

n = int(input())

queue = deque()

for _ in range(n):
    command = input().strip().split(' ')
    if command[0].startswith('append'):
        op, value = command
        getattr(queue, op)(value)
    elif command[0].startswith('pop'):
        getattr(queue, command[0])()

print(' '.join(queue))