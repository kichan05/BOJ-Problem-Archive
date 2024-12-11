str_ = input()

mo = "MOBIS"

result = True

for i in mo:
    result = result and i in str_
    
if(result):
    print("YES")
else:
    print("NO")
