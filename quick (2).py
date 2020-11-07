import random
def partition(arr, start, end):
 
    #Initializing Pivot Index & Iteration index of list 
    pivot = start
    i = start + 1
    j = end

#This Loop is providing iterations for i <= j. because if this condition is true
# then we have to continue with the same i and j.
# Else if we have to Break the Loop and Swap the Pivot value to its Correct Position. 
    while True:

        while i <= j and arr[i]<=arr[pivot]:
            i += 1

        while i <= j and arr[j]>=arr[pivot]:
            j -= 1
        
        
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j


def quicksort(arr, start, end):
    if start < end:

        #First i have to find the point from where the list can be divided into sub lists.
        partition_point = partition(arr, start, end)
        
        #After finding partition point repeat the process for the left sub array
        quicksort(arr, start, partition_point-1)
        
        #After finding partition point repeat the process for the right sub array
        quicksort(arr, partition_point+1, end)
arr = []
for i in range(10):
    arr.append(random.randint(10,200))
quicksort(arr, 0, len(arr)-1)
print(arr)