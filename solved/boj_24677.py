n = int(input())

sum_ = 0

for i in range(1, n - 1):
    sum_ += (n - i) ** 2 - (n - i)
    
print(sum_ // 2)
print(3)
