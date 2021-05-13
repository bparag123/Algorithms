def permutations(a):
    
    if len(a) == 0:
        return [ [] ]
    current_ele = a[0]
    remaining_perms = permutations(a[1:])
    
    all_perms = []

    for perm in remaining_perms:
        for i in range(len(perm)+1):
            all_perms.append(perm[:i] + [current_ele] + perm[i:])
    
    return all_perms
a = ['a', 'b', 'c', 'd']
print(permutations(a))
print("Total Permutations : ",len(permutations(a)))


