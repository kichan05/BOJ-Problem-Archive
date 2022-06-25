N = int(input())

list_ = []

for i in range(N):
    list_.append(int(input()))
    
    
list_.sort()
list_.reverse()

sum_ = 0
for n, i in enumerate(list_):
    sum_ += max(0, i - n)
    
print(sum_)
