#!/usr/bin/env python3

from sys import argv, stdin, stdout

# Load Maze
baseMaze = []
while True:
    line = stdin.readline()
    if not line:
        break
    line = line.strip()
    baseMaze.append(line)
#    print(line)
#print()

# Maze Size
w = len(baseMaze[0]) 
h = len(baseMaze)

end_col = dW = w//4
end_row = dH = h//2

end_col -= 1
end_row -= 1

queue = [[0,0]]
seen = [[False for x in range(dW)] for y in range(dH)]
seen[0][0] = True
best = [[[-1,-1] for x in range(dW)] for y in range(dH)]
maze = [[[False,False,False,False] for x in range(dW)] for y in range(dH)]

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Load Maze
for y in range(h-1):
    for x in range(w-1):
        if y%2==1 and x>0 and x%4==0:
            dY = (y-1)//2
            dX = (x//4)-1
            if baseMaze[y][x] == '|':
                maze[dY][dX][RIGHT] = False
                maze[dY][dX+1][LEFT] = False
            else:
                maze[dY][dX][RIGHT] = True
                maze[dY][dX+1][LEFT] = True
        elif y>0 and y%2==0 and x%4==2:
            dY = (y//2)-1
            dX = (x-2)//4
            if baseMaze[y][x] == '-':
                maze[dY][dX][DOWN] = False
                maze[dY+1][dX][UP] = False
            else:
                maze[dY][dX][DOWN] = True
                maze[dY+1][dX][UP] = True

# Solve Maze
while len(queue) > 0:
    y, x = queue.pop(0)
    for wall, (next_y, next_x) in [
        [RIGHT,[y,x+1]],
        [LEFT,[y,x-1]],
        [UP,[y-1,x]],
        [DOWN,[y+1,x]]]:

        if maze[y][x][wall]:
            if not seen[next_y][next_x]:
                best[next_y][next_x] = [x, y]
                queue.append([next_y, next_x])
            seen[next_y][next_x] = True


# Run
solution = [[False for x in range(dW)] for y in range(dH)]
solution[end_row][end_col] = True
x = end_col
y = end_row
while x>0 or y>0:
    x,y = best[y][x]
    solution[y][x] = True

if not solution[0][0]:
    print("No solution!")
    exit()

# Print Maze
for y in range(h):
    for x in range(w):
        if x%4==2 and y%2==1:
            dX = (x-2)//4
            dY = (y-1)//2
            if solution[dY][dX]:
                stdout.write('@')
            else:
                stdout.write(' ')
        else:
            stdout.write(baseMaze[y][x])
    stdout.write("\n")
