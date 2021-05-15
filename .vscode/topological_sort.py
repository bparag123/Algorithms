#Topological sort is a kind f technique which stores data as...
# Parent Node Should be First in Order and after that all Child Nodes Should Lie
# This is Applied on Directed Acyclic Graph 
class Node:
    def __init__(self, node):
        self.node = node
        self.connected_nodes = []
    
    def connect(self, node):
        self.connected_nodes.append(node)
        


class Graph:
    def __init__(self):
        self.nodes = []
        
    def add_new_node(self, node):
        self.nodes.append(node)

    def topologicalSort(self, startNode, topological_order, visited):
        visited.append(startNode)
        # Here I'm Traversing in the Depth of Each Node to find the Leaf Node
        for adjecency in startNode.connected_nodes:
            self.dfs(adjecency, visited , topological_order)
        #above for loop will complete all the Child Nodes Depth Traversal 
        topological_order.append(startNode)
    def dfs(self, start, visited, topological_order):
        # Base Case 
        if start.connected_nodes == []:
            #This is the case Where The Curent Node is Leaf So append it to the Ordering
            topological_order.append(start)
            return
        else:
            visited.append(start)
            for adjecency in start.connected_nodes:
                try:
                    #Here it will Throw error is adjecency is not found
                    #and if not found then we have to run except part.....Yes Thats Good
                    visited.index(adjecency)
                    
                except:
                    self.dfs(adjecency, visited, topological_order)
            #above Loop Will be Completed When Depth of the Graph for Current Node is Achieved.
            #So after that it is Safe to add Current node to the Order 
            topological_order.append(start)
            return


rajkot = Node('Rajkot')
ahmedabad = Node('Ahmedabad')
surat = Node('Surat')
baroda = Node('Baroda')
gandhinagar = Node('Gandhinagar')
kutch = Node('Kutch')

g = Graph()
g.add_new_node(rajkot)
g.add_new_node(ahmedabad)
g.add_new_node(surat)
g.add_new_node(baroda)
g.add_new_node(gandhinagar)
g.add_new_node(kutch)

rajkot.connect(ahmedabad)
ahmedabad.connect(baroda)
ahmedabad.connect(kutch)
kutch.connect(gandhinagar)
baroda.connect(surat)


visited = []
topological_order = []
g.topologicalSort(rajkot, topological_order, visited)
#in Login i have Implemented the order in Reverse Manner First append all Child Then Parent
# That is why it is required to reverse here.
topological_order.reverse()
for i in topological_order:
    print(i.node)