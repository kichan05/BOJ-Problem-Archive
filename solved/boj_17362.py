n = int(input())

n -= 1

A = n % 8

if(A == 0):
    print(1)
elif(A == 1 or A == 7):
    print(2)
elif(A == 2 or A == 6):
    print(3)
elif(A == 3 or A == 5):
    print(4)
elif(A == 4):
    print(5)
