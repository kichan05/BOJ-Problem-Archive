list_ = [64]

X = int(input())

while (sum(list_) > X):
  list_.sort()
  sum_ = list_[0] / 2 + sum(list_[1:])
  list_[0] = int(list_[0] / 2)
  
  if(sum_ < X):
    list_.append(list_[0])

  # print(list_)



print(len(list_))
