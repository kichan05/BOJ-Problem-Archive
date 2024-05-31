[N = int(input())
A = list(map(int, input().split()))
X, Y = map(int, input().split())

count1 = round(X / 100 * N)
count2 = sum(list(map(lambda x : x >= Y, A)))

print(count1, count2)

