n = input()
if int(n) < 1000:
    n = (str('0') + str(n))
if int(n) < 100:
    n = (str('00') + str(n))
if str(n[0] + n[1]) == str(n[3] + n[2]):
    print(1)
else:
    print(9999)
