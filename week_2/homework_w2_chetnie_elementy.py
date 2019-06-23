x = int(input())
even_numbers = 0
while x != 0:
    if x % 2 == 0:
        even_numbers += 1
    x = int(input())
print(even_numbers)
