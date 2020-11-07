import random

def insertion(arr):
    
    n = len(arr)
    for i in range(1,n):
        #Copying the actual value of next unsorted element. Bcoz it is now backed up and we can use to store 
        # it on its actual position.
        temp = arr[i]
        #now starting compare the temp with sorted parts from right -> left anf find it's 
        #correct position. 
        j = i-1
        while j>=0 and arr[j] > temp:
            #if sorted ele > temp then we have to step up the value of sorted ele.
            #and create the hole for temp on left side
            arr[j+1] = arr[j]
            j-=1
        #Upper loop will terminated when the temp > any sorted value.
        #so that's how i got the correct position of the temp so lets store it.
        #here j+1 is used bcoz in last execution of loop j is decremented.
        #so it is incremented with 1 here.
        arr[j+1] = temp

    print("Output ->", arr)
arr = []
for i in range(5):
    arr.append(random.randint(0,20))
print("Input ->", arr)
insertion(arr)