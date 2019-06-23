n = int(input())
x = 0
summa = n**2
while x != n and n != 1:
    summa += x**2
    x += 1
print(summa)
