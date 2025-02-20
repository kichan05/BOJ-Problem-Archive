N, M = map(int, input().split())
snow = [1] + list(map(int, input().split()))

def fun(size, index, time):
    if(time >= M or index == N):
        return size
    
    s1, s2 = 0, 0
    if(index + 1 <= N):
        s1 = fun(size + snow[index + 1], index + 1, time + 1)
    
    if(index + 2 <= N):
        s2 = fun(size // 2 + snow[index + 2], index + 2, time + 1)
        
    return max(s1, s2)

print(fun(1, 0, 0))
