import sys

N = int(input())

users = []

for i in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    
    users.append({
        "age" : age,
        "name" : name,
        "id" : i
    })
    
users = sorted(users, key= lambda x: (x["age"], x["id"]))

for u in users:
    sys.stdout.write(f'{u["age"]} {u["name"]}\n')
