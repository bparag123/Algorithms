import random
def counting(arr, divider):
    counter_arr = [0] * 10
    output_arr = [0] * len(arr)

    #counting the elememts
    for i in range(len(arr)):
        counter_arr[ (arr[i] // divider) % 10 ] += 1
    
    #now updating the counter value.
    #we do this because of after updating we can know the actual position of ele.

    for i in range(1,10):
        counter_arr[i] += counter_arr[i-1]
    
    # now for stable sorting we are travesing the array from right -> left
    # bcoz first occurence of same number always should be first
    
    for i in range(len(arr)-1, -1, -1): 
        output_arr[  counter_arr[ (arr[i] // divider) % 10]  - 1  ] = arr[i]
        counter_arr[ (arr[i] // divider) % 10] -= 1
    
    #copying the output array to the main array which will used in next pass
    for i in range(len(arr)):
        arr[i] = output_arr[i]

def radix(arr):
    m = max(arr)
    
    divider = 1
    while m / divider > 0:
        counting(arr, divider)
        divider *= 10
arr = []
for i in range(5):
    arr.append(random.randint(0,20))
print(arr)
radix(arr)
print(arr)