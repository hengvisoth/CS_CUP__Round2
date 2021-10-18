
n , k = map(int,input().split())
import timeit

start = timeit.default_timer()

cordinate_queen = []
posible_move = []
cells = []
count = 0
for a in range(0,k) :
     i , j = map(int,input().split())
     cordinate_queen.append([i,j])
print(cordinate_queen)
# possible move
for i in range (0,len(cordinate_queen)) :
     for j in range (-1,2) :
          for k in range(-1,2):
               ls1 = [cordinate_queen[i][0]+j,cordinate_queen[i][1]+k]
               posible_move.append(ls1)

# generate all cell
for m in range(1,n+1) :
     for j in range(1,n+1) :
          cell = [m,j]
          cells.append(cell)

# compare whether it is in cell or not
for z in range(0,len(cells)):
     if cells[z] not in posible_move:
          count +=1

print(count)
print(cells)
print(posible_move)
stop = timeit.default_timer()
print(stop-start)
