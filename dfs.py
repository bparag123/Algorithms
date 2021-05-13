class Node:
    def __init__(self, root):
        self.root = root
        self.right = None
        self.left = None

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

#Simple DFS Traversal USING STACK

def dfs_print(root):
    stack = [root]
    while len(stack) > 0 :
        current = stack[-1]
        print(current.root, end=" ")
        
        if current.right != None:
            stack.append(current.right)
        
        if current.left != None:
            stack.append(current.left)
        stack.remove(current)
        

dfs_print(a)

# DFS for Searching Some Result

# target = 'x'
# def dfs_print(root, target):
#     stack = [root]
#     found = False
#     while len(stack) > 0 :
#         current = stack[-1]
#         if current.root == target:
#             print("True")
#             found = True
#             break        
#         if current.right != None:
#             stack.append(current.right)
#         if current.left != None:
#             stack.append(current.left)
#         stack.remove(current)
#     if not found:
#         print("False")
        

# dfs_print(a, target)


#DFS Using RECURSION with ALL Type Of Traversals

# type = input("Which Travesal you Want?\n(Options:\tIN\tPOST\tPRE)\n")
# def generate_DFS(root, type):
#     #Base Case
#     if root == None:
#         return
#     else:
#         if type == "IN":
#             generate_DFS(root.left, type)
#             print(root.root, end=" ")
#             generate_DFS(root.right, type)
#         elif type == "PRE":
#             print(root.root, end=" ")
#             generate_DFS(root.left, type)
#             generate_DFS(root.right, type)
#         elif type == "POST":
#             generate_DFS(root.left, type)
#             generate_DFS(root.right, type)
#             print(root.root, end=" ")
#         else:
#             print("Please Enter Valid Choice")
            
# generate_DFS(a, type)


