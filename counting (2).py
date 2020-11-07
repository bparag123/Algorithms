import random
import datetime
def counting(arr, m):
    #Here we have to create array to store the count of the number with size of maximum number.
    counter_arr = [0]*(m+1)
    
    #Storing the Count of the particular element.
    for i in range(len(arr)):
        counter_arr[arr[i]] += 1

    #Creating Resultant array
    output_arr = []

    #Copying the Data Frequency-wise in Output Array
    for i in range(len(counter_arr)):
        if counter_arr[i]>0:
            while counter_arr[i]>0:
                output_arr.append(i)
                counter_arr[i] -= 1

    return output_arr
    
def max(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max


arr = []
for i in range(15):
    arr.append(random.randint(0,500))

print("Input ->",arr)
m = max(arr)
result = counting(arr, m)
print("Output ->", result)

