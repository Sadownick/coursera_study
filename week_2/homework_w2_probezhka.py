x = int(input())
y = int(input())
z = 1
while (x * 0.1 + x) < (y + x * 0.1) and x != y:
    x += x * 0.1
    z += 1
print(z)
