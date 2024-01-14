import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pre = [[0] * (M + 1)]

for i in range(1, N + 1):
    row = list(map(int, input().split()))
    
    pre_row = [0]
    # row_sum = 0
    for j in range(1, M + 1):
        # row_sum += row[j - 1]
        pre_row.append(pre[i - 1][j] + pre_row[-1] + row[j - 1])
        
    pre.append(pre_row)
    
for row in pre:
    print(row)

K = int(input())

