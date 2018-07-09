from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    boxes = deque(map(int, input().strip().split()))
    last_box = 2**31

    while len(boxes) > 0:
        left = boxes[0]
        right = boxes[len(boxes) - 1]

        if left == right:
            if left <= last_box:
                last_box = boxes.popleft()
            else:
                print("No")
                break
                
        else:
            if left > right and left <= last_box:
                last_box = boxes.popleft()
            elif right > left and right <= last_box:
                last_box = boxes.pop()
            else:
                print("No")
                break

    else:
        print("Yes")
