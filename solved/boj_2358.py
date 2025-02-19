N = int(input())

x_list = {}
y_list = {}

count = 0

for _ in range(N):
    x, y = tuple(input().split())
    
    if(x not in x_list):
        x_list[x] = 0
    
    x_list[x] += 1

    if(y not in y_list):
        y_list[y] = 0
    
    y_list[y] += 1
    
for p, v in x_list.items():
    if(v >= 2):
        count += 1
        
for p, v in y_list.items():
    if(v >= 2):
        count += 1
        
print(count)
