format_ = input()

count = 1

if(format_[0] == "d"):
    count *= 10
else:
    count *= 26

for i in range(1, len(format_)):
    if(format_[i] == "d"):
        if(format_[i] == format_[i - 1]):
            count *= 9
        else:
            count *= 10
            
    else:
        if(format_[i] == format_[i - 1]):
            count *= 25
        else:
            count *= 26
    count %= 1000000009
    
print(count)
