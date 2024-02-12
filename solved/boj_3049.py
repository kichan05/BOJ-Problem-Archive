from math import factorial as ft

n = int(input())

if(n == 3):
    print(0)
else:
    print(ft(n) // ft(4) // ft(n - 4))
