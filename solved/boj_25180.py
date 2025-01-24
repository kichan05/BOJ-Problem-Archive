N = int(input())

count = N // 18 * 2
N %= 18

if(0 < N < 10):
    count += 1
elif(10 <= N < 19 and N % 2 == 0):
    count += 2
elif(10 <= N < 19):
    count += 3
    
print(count)
