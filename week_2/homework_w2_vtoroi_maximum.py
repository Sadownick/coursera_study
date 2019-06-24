x = int(input())
max_number = x
previous_number = 0
while x != 0:
    x = int(input())
    if x >= max_number:
        previous_number = max_number
        max_number = x
    elif max_number > x >= previous_number:
        previous_number = x
print(previous_number)
