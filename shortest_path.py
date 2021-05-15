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


    #Path Rearrangment with help of Queue
    # def generate_path_from_record(self, visited, startNode, endNode):
        
    #     path = []
        
    #     queue = [ endNode ]

    #     while len(queue) > 0:
    #         current = queue.pop(0)

    #         if current in visited:
    #             queue.append(visited[current])
    #             path.append(current)
        
    #     return path


    #Recusive Path Rearrangment
    def generate_path_from_record(self, visited, startNode, endNode):
        
        # Here Visited is a dictionary contains
        # key as Currently Visit City
        # and value is City from which we are coming

        #Here I'm Solving The Problem from Reverse Pattern.
        #First I'm getting the end node and after that checking from where i'm coming from.

        if visited[endNode] == startNode:
            return [endNode, startNode]
        path = []
        # Let's add Current Node to Path Because the parent of This Node is not Starting Point
        path.append(endNode)
        #Recursively Find Upper Level to find from Which City we came to visited[endNode] City.
        path += self.generate_path_from_record(visited, startNode, visited[endNode])
        return path

    def bfs(self, startNode, endNode):
        queue = [ startNode ]
        visited = {}
        visited[startNode] = None
        while len(queue) > 0:

            current = queue.pop(0)


            for adjecent_node in current.connected_nodes:
                
                if not adjecent_node in visited:
                    visited[adjecent_node] = current
                    queue.append(adjecent_node)
        return self.generate_path_from_record(visited, startNode, endNode)

    


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



data = g.bfs(ahmedabad, surat)
data.reverse()

for i in data:
    print(i.node, end=" ")