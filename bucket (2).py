import random, math

def selection_sort(a):
    
    if len(a)>1:
        for j in range(len(a)):
            min_index = j
            for k in range(j+1, len(a)):
                if a[min_index] > a[k]:
                    min_index = k
            
            a[j], a[min_index] = a[min_index], a[j]
              
    return a

def bucket(arr):
    n = len(arr)
    counter_arr = [0]*10
    for i in arr:
        # Here first i checking the element of counter array is array or not.
        #from try-except i am able to know it is array of not.
        #after checking if the element is array then append the new sub element into this subarray
        #else create one subarray and add it into the counter array
        try:
            len(counter_arr[ math.floor(i*10)])
            counter_arr[ math.floor(i*10) ].append(i)
            
        except:
            counter_arr[ math.floor(i*10) ] = [i]
            
    for i in range(len(counter_arr)):
        try:
            len(counter_arr[i])
            #Here we have to sort the subarray.
            
            #here i have created one function which returns a sorted array
            counter_arr[i] = selection_sort(counter_arr[i])
        except:
            pass
    final_arr = []
    for i in counter_arr:
        try:
            len(i)
            for j in i:
                final_arr.append(j)
        except:
            pass
    print("Output ->" , final_arr)
arr = []

for i in range(10):
    arr.append(round(random.random(), 2))
    
print("Input ->", arr)
bucket(arr)


