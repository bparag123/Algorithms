class Node:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')


a.left = b
a.right = c
b.left = d
c.left = e
b.right = f
c.right = g

# Simple Traversal for BFS

def bfs_print(root):
    
    current = [root]
    while len(current) > 0:
        print(current[0].root, end=" ")
        if current[0].left != None:
            current.append(current[0].left)
        if current[0].right != None:
            current.append(current[0].right)
        current.remove(current[0])
bfs_print(a)


#BFS Program to Search Specific Value

# target = 'x'
# def bfs_print(root, target):
#     found = False
#     current = [root]
#     while len(current) > 0:
#         if current[0].root == target:
#             print("True")
#             found = True
#             break
#         if current[0].left != None:
#             current.append(current[0].left)
#         if current[0].right != None:
#             current.append(current[0].right)
#         current.remove(current[0])
#     if not found:
#         print("False")
# bfs_print(a, target)

#BFS To Find Sum

# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)
# f = Node(6)
# g = Node(7)

# a.left = b
# a.right = c
# b.left = d
# c.left = e
# b.right = f
# c.right = g

# def bfs_print(root):
#     sum = 0
#     current = [root]
#     while len(current) > 0:
#         sum += current[0].root
#         if current[0].left != None:
#             current.append(current[0].left)
#         if current[0].right != None:
#             current.append(current[0].right)
#         current.remove(current[0])
#     print("Total Sum is ", sum)
# bfs_print(a)