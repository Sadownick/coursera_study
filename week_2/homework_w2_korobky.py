a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
if a > b:
    (a, b) = (b, a)
if b > c:
    (b, c) = (c, b)
if a > b:
    (a, b) = (b, a)
print(a, b, c)
