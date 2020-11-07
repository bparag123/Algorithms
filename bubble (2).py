import random

def bubble(arr):
    
    n= len(arr)

    #Here iterate through all the ele. of array in outer for loop
    for i in range(n-1):
        #in inner for loop we have to compare two serial value through the array
        #and help to the maximum value to reach the last part of the unsorted array.
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = []
for i in range(5):
    arr.append(random.randint(0,20))
print("Input->", arr)
bubble(arr)
print("Output->", arr)