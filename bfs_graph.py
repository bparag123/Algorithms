class Node:
    def __init__(self, node):
        self.node = node
        self.connected_nodes = []
    
    def connect(self, node):
        self.connected_nodes.append(node)
        #Here This Statement is for Undirected Graph as i wrote a-b == b-a
        node.connected_nodes.append(self)


class Graph:
    def __init__(self):
        self.nodes = []
        
    def add_new_node(self, node):
        self.nodes.append(node)


    def bfs(self,startNode):
        queue = [ startNode ]
        visited = []
        visited.append(startNode)
        while len(queue) > 0:
            
            current_node = queue.pop(0)
            for adjecent_node in current_node.connected_nodes:
                if not adjecent_node in visited:
                    
                    visited.append(adjecent_node)
                    queue.append(adjecent_node)
            
        return visited


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
rajkot.connect(baroda)
rajkot.connect(kutch)
kutch.connect(gandhinagar)
kutch.connect(baroda)
baroda.connect(surat)
gandhinagar.connect(surat)

for i in g.bfs(ahmedabad):
    print(i.node, end=" ")