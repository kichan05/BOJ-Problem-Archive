input()

str_ = input()
sum_ = 0
num = 0

for i in str_:
    if(ord('0') <= ord(i) <= ord('9')):
        num *= 10
        num += int(i)
    else:
        sum_ += num
        num = 0
        
sum_ += num
print(sum_)
