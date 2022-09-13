n = int(input())

fibo = [0, 1]

for i in range(1, abs(n) + 1):
    fibo.append((fibo[i] + fibo[i - 1]) % 1000000000)
    
if(n < 0 and abs(n) % 2 == 0):
    print("-1")
    
elif(n == 0):
    print("0")
    
else:
    print("1")
    
    
print(fibo[abs(n)])
# print(fibo)
