A, B = map(int, input().split())

if(A > B):
    print(2 * B + 1)
elif(A == B):
    print(2 * (B - 1) + 1)
elif(A < B):
    print(2 * (A - 1) + 1)
