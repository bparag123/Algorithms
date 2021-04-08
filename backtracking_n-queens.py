queens = int(input())
a= [[0 for i in range(queens)] for j in range(queens)]


def is_attacked(row,col,a):
    
    for i in range(len(a)):
        if a[row][i] == 1 or a[i][col] == 1:
            return True
    for i in range(len(a)):
        for j in range(len(a)):
            if i+j == row+col or i-j == row-col:
                if a[i][j] == 1:
                    return True
    return False


def set_queen(a, queens):
    if queens==0:
        return True
    else:
        for i in range(len(a)):
            for j in range(len(a)):
                if not is_attacked(i,j,a) and a[i][j]!=1:
                    a[i][j] = 1
                    if set_queen(a,queens-1):
                        return True
                    a[i][j] = 0
        return False


set_queen(a,queens)
for i in range(queens):
    for j in range(queens):
        print(a[i][j], end=" ")
    print("\n")
