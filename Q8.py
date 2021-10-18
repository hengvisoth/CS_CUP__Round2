n = int(input())
raw_ls = []
ls = []
# input
for num_coin in range(n):
    num_coin = list(map(int,input().split()))
    raw_ls.append(num_coin)
# convert all the input to un-nested list
for item in raw_ls :
    for element in item :
      ls.append(element)
front_size = []
back_size = []
for x in range(0,len(ls)) :
    if x%2 == 0 :
        front_size.append(x)
    else :
        front_size.append(x)


