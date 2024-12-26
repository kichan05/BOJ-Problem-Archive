# print(ord("A"), ord("Z"))
# print(ord("a"), ord("z"))
# A: 65, B: 90
# a: 97, b: 122

def toNum(x):
    asci = ord(x)
    
    if(ord("a") <= asci and asci <= ord("z")):
        return asci - 70
        
    if(ord("A") <= asci and asci <= ord("Z")):
        return asci - 64
        
    if(asci == ord(" ")):
        return 0
    

N = int(input())

nums = list(map(int, input().split()))
text = list(map(toNum, input()))

nums.sort()
text.sort()

flag = True

for n, i in enumerate(nums):
    if(i != text[n]):
        flag = False
        break
    
if(flag):
    print("y")
else:
    print("n")
