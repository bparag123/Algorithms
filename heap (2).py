import random

def heapify(a, n, i):
    max = i
    
    # Assigning Left and Right Childs 
    left = 2 * i + 1
    right = 2 * i + 2

    #Check if Left exist and Greater that root 
    if n > left  and a[left] > a[i]:
        max = left
    

    #Check if Right exist and Greater that root
    if n > right  and a[right] > a[max]:
        max = right
    
    #Swapping if Left Or Right Child has Greater value Then root
    if max != i:
        a[max], a[i] = a[i], a[max]
        heapify(a, n, max)

def heapsort(a):
    
    n = len(a)

    #Here Staring Parent is n//2 -1 . So we start with this as a First Parent.

    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n , i)
    
    # After this for loop the heapified tree is generated.
    #now as per the algo. we have to swap the highest indexed value with the 0th index value.
    
    for i in range(n-1, 0, -1):
        #by doing this step it can broke heapify structure so againg heapifying the tree.
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)


a = []
for i in range(5):
    a.append(random.randint(1,10))
print("Input",a)
heapsort(a)
print("Output",a)