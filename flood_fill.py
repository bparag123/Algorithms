a = [
    [0,0,1,1,0],
    [0,1,1,1,0],
    [1,0,1,0,0],
    [1,0,1,1,0],
    [0,0,1,1,1],
]

def f(a, row, col):
    if row<0 or col<0 or row>len(a)-1 or col > len(a)-1 or a[row][col] == 0 or temp[row][col] == False:
        return 0
    else:
        a[row][col] = 100
        temp[row][col] = False
        return 1 + f(a, row+1, col) + f(a, row-1, col) + f(a, row, col+1) + f(a, row, col-1)
ans = 0
temp= [ [True for j in range(5)] for i in range(5) ]
max_length = 0
count = 0
for i in range(5):
    for j in range(5):
        ans = f(a, i, j)
        if ans>0:
            count += 1
        if ans > max_length:
            max_length = ans

print("Maximum Length Forest ", max_length)
print("Total Forest  ", count)
