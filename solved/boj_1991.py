N = int(input())

tree = {}
tree_ = {}

for i in range(ord('A'), ord('A') + N):
    tree_[chr(i)] = 0

for i in range(N):
    me, left, right = input().split()
    
    tree[me] = {"left" : left, "right" : right}
    

fitstList = []
middelList = []
lastList = []

def fitst(node):
    fitstList.append(node)
    
    if(tree[node]["left"] != "."):
        fitst(tree[node]["left"])
        
    if(tree[node]["right"] != "."):
        fitst(tree[node]["right"])
        
def middle(node):
    if(tree[node]["left"] != "."):
        middle(tree[node]["left"])
        
    middelList.append(node)
        
    if(tree[node]["right"] != "."):
        middle(tree[node]["right"])
        
def last(node):
    if(tree[node]["left"] != "."):
        last(tree[node]["left"])
    
    if(tree[node]["right"] != "."):
        last(tree[node]["right"])
    
    lastList.append(node)
        
fitst("A")
middle("A")
last("A")
print("".join(fitstList))
print("".join(middelList))
print("".join(lastList))
