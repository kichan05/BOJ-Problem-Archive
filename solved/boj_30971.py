for i in range(1, 10):
    print(f"? A {i}", flush=True)
    
    result = int(input())
    if(result == 1):
        A = i
        break
for i in range(1, 10):
    print(f"? B {i}", flush=True)
    
    result = int(input())
    if(result == 1):
        B = i
        break
    
print(f"! {A + B}")
