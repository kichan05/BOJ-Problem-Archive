import sys
sys.setrecursionlimit(10**6)

n = int(input())

list_ = [-1 for i in range(n + 1)]

def fibo(n):
    if n == 0:
        return 0
    
    if n <= 2:
        return 1
        
    if list_[n] != -1:
        return list_[n]
    
    list_[n] = fibo(n - 1) + fibo(n - 2)
    
    return list_[n]
    
    

print(fibo(n))
