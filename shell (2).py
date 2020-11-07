import random

def shell(arr):
    n = len(arr)

    gap = n // 2

    while gap > 0:

        # Here we started iteration in array with gap
        for i in range(gap, n):

            #Copying the actual value of next unsorted element. Bcoz it is now backed up and we can use to store 
            # it on its actual position.
            temp = arr[i]
            #now starting compare the temp with sorted parts from right -> left anf find it's 
            #correct position.
            j = i-gap

            while j >= 0 and arr[j]>temp:
                #if sorted ele > temp then we have to step up the value of sorted ele.
                #and create the hole for temp on left side
                arr[j+gap] = arr[j]
                j -= gap
            #Upper loop will terminated when the temp > any sorted value.
            #so that's how i got the correct position of the temp so lets store it.
            #here j+gap is used bcoz in last execution of loop j is decremented.
            #so it is incremented with gap here.
            arr[j+gap] = temp
        #reducing the gap
        gap = gap // 2
arr = []
for i in range(5):
    arr.append(random.randint(0,20))
print("Input->", arr)
shell(arr)
print("Output->", arr)