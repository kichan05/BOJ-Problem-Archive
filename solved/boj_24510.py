C = int(input())

max_ = 0

for _ in range(C):
    code = input()
    
    f = max(code.count("for"), 0)
    w = max(code.count("while"), 0)
    
    sum_ = f + w
    
    max_ = max(sum_, max_)
    
    # print(f, w, sum_)
    
print(max_)
