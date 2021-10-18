n = int(input())
ls = []
for i in range(1,n+1):
    ls.append(i)
# from observation every three consecutive value will always turn into 1 2 0
# so what we have to do is to convert every 3 consecutive number to 0
nLoop = len(ls) // 3
for j in range(len(ls),0,-3) :
    if j < 3 :
        break
    ls[j-1],ls[j-2],ls[j-3] = 0,2,1

res = sum(ls)

print(res )


