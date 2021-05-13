#This is Combination Creation Program using Recursion


def combinations(a):
    #base case
    if len(a) == 0:
        return [[]]

    else:
      
        result = []
        current_element = a[0]
        #Call Recursive Function to Take Combinations for Remaining elements
        remaining_combinations = combinations(a[1:])
        result.extend(remaining_combinations)
      
        #work for current Function Call is to append Current Element


        for comb in remaining_combinations:
            result.append(comb + [current_element])
        return result        

a= [1,2,3,4,5]
x = combinations(a)
for c in x:
    print(c)
print("Total Combinations : ",len(x))