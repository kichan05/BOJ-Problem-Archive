A, K = map(int, input().split())

count = [-1 for i in range(K + 1)]
count[A] = 0

queue = [A]

while len(queue) != 0:
    num = queue[0]
    del queue[0]
    
    num1 = num + 1
    num2 = num * 2
    
    if(num1 == K or num2 == K):
        print(count[num] + 1)
        break
    
    if(num1 < K and count[num1] == -1):
        queue.append(num1)
        count[num1] = count[num] + 1
    
    if(num2 < K and count[num2] == -1):
        queue.append(num2)
        count[num2] = count[num] + 1
