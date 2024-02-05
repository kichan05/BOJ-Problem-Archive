n = int(input())

code1 = [0, 1, 1, 2, 3]

for i in range(5, n + 1):
    code1.append(code1[i - 1] + code1[i - 2])
    
print(code1[-1])
print(n - 2)
