N = int(input())
str_ = list(input())

code = {
    "A" : {"A": "A", "G": "C", "C" : "A", "T": "G"},
    "G" : {"A": "C", "G": "G", "C" : "T", "T": "A"},
    "C" : {"A": "A", "G": "T", "C" : "C", "T": "G"},
    "T" : {"A": "G", "G": "A", "C" : "G", "T": "T"},
}

while N >= 2:
    an = str_[-1]
    an_1 = str_[-2]
    
    del str_[-1]
    del str_[-1]
    
    str_.append(code[an][an_1])
    N -= 1
    
print(str_[0])
