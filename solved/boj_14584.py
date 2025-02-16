str_ = input()
N = int(input())

dict_ = []

for _ in range(N):
    dict_.append(input())


for i in range(1, ord("z") - ord("a") + 2):
    new = ""
    for ch in str_:
        new_ch = ord(ch) + i
        if(new_ch > ord("z")):
            new_ch -= ord('z') - ord('a') + 1
        
        new += chr(new_ch)
        
    
    for word in dict_:
        if(word in new):
            print(new)
            exit(0)
