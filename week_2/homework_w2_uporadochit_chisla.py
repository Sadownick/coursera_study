a, b, c = int(input()), int(input()), int(input())
if a >= b >= c:
    (c, a) = (a, c)
elif a >= c >= b:
    (a, b, c) = (b, c, a)
elif c >= a >= b:
    (a, b, c) = (b, a, c)
elif b >= a >= c:
    (a, b, c) = (c, a, b)
print(a, b, c)
