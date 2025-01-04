A, B = map(int, input().split())

def number_length(number):
    count = 0
    
    while(number):
        number //= 10
        count += 1
        
    return count

a_length = number_length(A)
b_length = number_length(B)

if(a_length > b_length):
    print(A // 10 ** b_length, end = "")
    A %= 10 ** b_length
    length = b_length

    
elif(a_length < b_length):
    print(B // 10 ** a_length, end = "")
    B %= 10 ** a_length
    
    length = a_length
else:
    length = a_length
    
for i in range(length - 1, -1, -1):
    print(A // 10 ** i % 10 + B // 10 ** i % 10, end = "")
