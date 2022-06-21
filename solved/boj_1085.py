x, y, w, h = tuple(map(int, input().split()))

list_ = []

list_.append(x)
list_.append(h - y)
list_.append(w - x)
list_.append(y)

print(min(list_))
