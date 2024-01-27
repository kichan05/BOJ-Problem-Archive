fibo_nums = [-1, 1, 1]

N = int(input())

for i in range(3, N + 1):
    fibo_nums.append(fibo_nums[i - 1] + fibo_nums[i - 2])
    
print(fibo_nums[N])
