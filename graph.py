#method-1 to achive Graph Data Structure
# By Using Vertices and Edges as a List

# vertices = ['a', 'b', 'c', 'd']
# edges = [
# ['a', 'b'],
# ['b', 'c'],
# ['a', 'c'],
# ['b', 'd'],
# ]

# # #Find Adjecent Nodes for partiular Node

# def find_adjecent(node):
#     adjecents = []
#     for edge in edges:
#         try:
#             found_at = edge.index(node)
#             if found_at == 0:
#                 adjecents.append(edge[1])
#             else:
#                 adjecents.append(edge[0])
#         except:
#             pass
#     return adjecents

# print(find_adjecent('a'))


#method-2 to achive Graph Data Structure
# By Using Adjecency Matrix
#Note: Here Adj. Matrix is Reflection for Diagonal if the Graph is Un-Directed.
# Because there is Two way connection a-b and b-a both can be possible.

# vertices = ['a', 'b', 'c', 'd']

# adjecency_matrix = [
#     [0,1,0,0],
#     [1,0,1,1],
#     [0,1,0,1],
#     [0,1,1,0],
# ]

# def find_adjecent(node):
#     adjecents = []

#     try:
#         get_node_index = vertices.index(node)
#         row_to_check = adjecency_matrix[get_node_index]
#         for i in range(len(row_to_check)):
#             if row_to_check[i]==1:
#                 adjecents.append(vertices[i])
#         return adjecents
#     except:
#         return "Given Node is Not Found"

    

# print(find_adjecent('a'))

#method-3 to achive Graph Data Structure
# By Using Adjecency Lists
# Here i'm storing the connected nodes with current Node


# class Node:
#     def __init__(self, node):
#         self.node = node
#         self.connected_nodes = []
    
#     def connect(self, node):
#         self.connected_nodes.append(node)
#         #Here This Statement is for Undirected Graph as i wrote a-b == b-a
#         node.connected_nodes.append(self)


# class Graph:
#     def __init__(self):
#         self.nodes = []
        
#     def add_new_node(self, node):
#         self.nodes.append(node)

#     def get_adjecent_nodes(self, node):
#         node_data = self.is_node_exists(node)
#         if node_data:
#             return node_data.connected_nodes

#     def is_node_exists(self, node):
#         for i in self.nodes:
#             if i.node == node:
#                 return i
#         return
    
    
#     def is_connected_with(self, node1, node2):
#         node_data_1 = self.is_node_exists(node1)
#         node_data_2 = self.is_node_exists(node2)
        
#         if node_data_1 and node_data_2:
#             if node_data_1 in node_data_2.connected_nodes:
#                 return True
#         return False

# node_a = Node('a')
# node_b = Node('b')
# node_c = Node('c')
# node_d = Node('d')

# g = Graph()
# g.add_new_node(node_a)
# g.add_new_node(node_b)
# g.add_new_node(node_c)
# g.add_new_node(node_d)

# node_a.connect(node_b)
# node_b.connect(node_d)
# node_b.connect(node_c)
# node_c.connect(node_d)

# user_entered_node =input("Enter Node for Which You Want to Find Adjecent...")

# if g.is_node_exists(user_entered_node):
#     for i in g.get_adjecent_nodes(user_entered_node):
#         print(i.node, end=" ")
#     print("\n")
# else:
#     print("You Entered Node is not Part of This Graph")

# print("Resuct Of Connection")
# print(g.is_connected_with('a', 'b'))


# method-4 to achive Graph Data Structure
# By Using Dictionary
# {
#     'a': ['b', 'c'],
#     'b': ['a'],
#     ....
# }
# Here Key is Current Node and valu is List of Connected Node