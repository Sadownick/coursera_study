x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(y1 - x1) % 2 == 0 and abs(y2 - x2) % 2 == 0:
    print('YES')
elif abs(y1 - x1) % 2 != 0 and abs(y2 - x2) % 2 != 0:
    print('YES')
else:
    print('NO')
