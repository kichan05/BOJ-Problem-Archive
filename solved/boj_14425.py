N, M = map(int, input().split())

str_list = []

for _ in range(N):
    str_list.append(input())

count = 0

for _ in range(M):
    s = input()
    
    if(s in str_list):
        count += 1
        
print(count)
