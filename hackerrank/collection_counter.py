from collections import Counter

x = int(input())

stock = Counter(input().split())

total = 0
n = int(input())
for _ in range(n):
    size, price = input().split()
    stock_qty = stock.get(size)
    if stock_qty and stock_qty > 0:
        total += int(price)
        stock.subtract([size])
print(total)