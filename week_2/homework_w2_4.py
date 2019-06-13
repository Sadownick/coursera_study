A = int(input())
if A % 400 == 0 or A % 100 != 0:
    if A % 4 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
