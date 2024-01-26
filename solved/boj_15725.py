poly = input()

if("x" not in poly):
    print(0)
    exit(0)

a = poly.split("x")[0]

if(a == ''):
    a = 1
if(a == '-'):
    a = -1


print(a)
