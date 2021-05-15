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

    def dfs(self, start, end, visited):
        # Base Case 
        if start.node == end.node:
            visited.append(end)
            return
        else:
            visited.append(start)
            for adjecency in start.connected_nodes:
                try:
                    #Here it will Throw error is adjecency is not found
                    #and if not found then we have to run except part.....Yes Thats Good
                    visited.index(adjecency)
                    
                except:
                    self.dfs(adjecency, end, visited)
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
kutch.connect(baroda)
baroda.connect(surat)


visited = []
g.dfs(ahmedabad, gandhinagar, visited)

for i in visited:
    print(i.node)