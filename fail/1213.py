count = [0 for i in range(ord('A'), ord('Z') + 1)]

name = input()

for i in name:
    count[ord(i) - ord("A")] += 1
    
count_ = count[::]

odd = ""

for key, value in enumerate(count):
    if(value % 2 != 0 and odd == ""):
        odd = key
        continue
        
    elif(value % 2 != 0 and odd != ""):
        print("I'm Sorry Hansoo")
        exit(0)

index = 0
while(index < len(count)):
    if(count[index] == 0):
        index += 1
        continue
    
    print(chr(index + ord("A")), end="")
    
    count[index] -= 1
    
    if(odd != index and count[index] == count_[index] // 2):
        index += 1
    if(odd == index and count[index] == count_[index] // 2 + 1):
        index += 1

if(odd != ""):
    print(chr(odd + ord("A")), end="")
    count[odd] -= 1
    
    
index -= 1

while(index >= 0):
    if(count[index] == 0):
        index -= 1
        continue
    
    print(chr(index + ord("A")), end="")
    
    count[index] -= 1
    
