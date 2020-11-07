import random

def selection(arr):
    n = len(arr)
    for i in range(n):
        #here initializing the index as index of minimum value.
        min_index = i
        for j in range(i+1, n):
            #now comparing the minindexed value with later indexed elements.
            #if anyone ele. has value less than min indexed value then update the min index
            if arr[j] < arr[min_index]:
                min_index = j
        #swapping the iterative value with updated min_indexed value
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Output->",arr)

arr= []
for i in range(5):
    arr.append(random.randint(0,20))
print("Input->",arr)
selection(arr)