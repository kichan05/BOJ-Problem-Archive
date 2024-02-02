T, S = map(int, input().split())

isLunch = 12 <= T <= 16
isAl = bool(S)

if(not isLunch or isAl):
    print(280)
else:
    print(320)
