a = ['a', 'b', 'c']

for i in range(2**len(a)):
    for j in range(len(a)):
        if i & 1<<j != 0:
            print(a[j], end=" ")
        else:
            print("_", end=" ")
    print("\n")