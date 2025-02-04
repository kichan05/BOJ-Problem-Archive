N = int(input())
str_ = input()

sum_ = 0

for n, ch in enumerate(str_):
    sum_ += (ord(ch) - ord("a") + 1) * 31 ** n
    
print(sum_ % 1234567891)
