import sys

n = int(input())

list_ = {}

for i in range(n):
    name, state = tuple(sys.stdin.readline().split())
    
    
    if(state == "enter"):
        list_[name] = True
    else:
        del list_[name]
            
            

list_ = list(list_.keys())            
list_.sort()
list_.reverse()


print("\n".join(list_))
