n , k = input().split()
ls = [int(x) for x in input().split()]
res = []
for i in range (0,len(ls)) :
    for j in range(i+1,len(ls)):

        a = ls[i] * ls[j]
        res.append(a)
print(sorted(res)[int(k)-1])
