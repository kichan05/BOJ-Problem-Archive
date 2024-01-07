alpha_list = ["c=","c-","dz=","d-","lj","nj","s=","z="]

str_ = input()

for alpha in alpha_list:
    while alpha in str_:
        str_ = str_.replace(alpha, "&")
        
        
print(len(str_))