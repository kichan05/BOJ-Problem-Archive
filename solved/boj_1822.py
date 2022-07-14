nA, nB = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))


diff = list(A - B)

diff.sort()

print(len(diff))

for i in diff:
    print(i, end=" ")
