class Node:
    def __init__(self, root):
        self.root = root
        self.right = None
        self.left = None

size = int(input("How Many Nodes You Have...?\n"))
print("Please Enter {} values".format(size))
arr = []
for i in range(size):
    arr.append(input())

nodes = []
for i in arr:
    nodes.append(Node(i))

n = len(nodes)

for i in range(0, n//2):
    
    current_root = nodes[i]
    current_root.left= nodes[(2*i)+1]
    current_root.right= nodes[(2*i)+2]
    

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
        


def bfs_print(root):
    
    current = [root]
    while len(current) > 0:
        print(current[0].root, end=" ")
        if current[0].left != None:
            current.append(current[0].left)
        if current[0].right != None:
            current.append(current[0].right)
        current.remove(current[0])

print("Breadth First Search")
bfs_print(nodes[0])
print("\n")
print("Depth First Search")
dfs_print(nodes[0])
