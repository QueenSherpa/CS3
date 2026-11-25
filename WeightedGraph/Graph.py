#HW3 Weighted Graph 
    #adjacency list
    #DFS
    #BFS


from collections import deque 

class Graph:
#version 1   
    def __init__ (self):
        self.vertices = [ ]
        
        self.adj_list =  { } 

    def add_vertex(self,newV):
        if newV in self.adj_list:
            print("This vertex already exists")
            return
        else:
            self.vertices.append(newV)
            self.adj_list[newV] = []

    def insert_sorted(self,vertex,neighbor,weight):
        neighbor_list = self.adj_list[vertex]
        new_edge = (neighbor, weight)

        #self.adj_list.push_back
        #existing_weight = self.new_edge(weight)
        for i, (existing_neighbor, existing_weight) in enumerate(neighbor_list):
            if existing_weight > weight:
                neighbor_list.insert(i, new_edge)
                return 
        neighbor_list.append(new_edge)
            
    def add_edge(self, v1,v2,weight):
        if not v1:
            print("v1 does not exist here")
            #exit 
            return
        if not v2:
            print("v2 does not exist")
            #exit
            return
        self.insert_sorted(v1,v2,weight)     #v1's list gets (v2,weight)
        self.insert_sorted(v2,v1,weight)     #v2's list gets (v1,weight)

    def display(self):
        for vertex in self.vertices:
            line = vertex + ":"
            for neighbor, weight in self.adj_list[vertex]:
                #line = line + " (" + neighbor +", " +  str(weight) + " )"
                line += f" ({neighbor}, {weight})"
            print(line)

    def bfs(self, start):
        visited = set()
        queue = deque()
        result = []

        visited.add(start)
        queue.append(start)
        
        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor, weight in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result 

                
    def dfs(self,start):
        visited = set()
        stack = []
        result = []

        stack.append(start) 

        while stack:
            current = stack.pop()
            if current in visited:
                continue 
            visited.add(current)
            result.append(current) 

            #push neighbors in reverse so the lowers-weight neighbor is popped first
            for neighbor, weight in reversed(self.adj_list[current]):
                if neighbor not in visited:
                    stack.append(neighbor)
        return result

def main():
    graph = Graph()

    factions = ["Cardassian Union", "United Federation of Planets","Bajoran","Romulan Empire","Klingon Empire","Borg","Tholian Assembly"]
    for f in factions:
        graph.add_vertex(f)

    edges = [
        ("Cardassian Union", "Romulan Empire", 42),
        ("Cardassian Union", "Bajoran", 14),
        ("United Federation of Planets", "Bajoran", 22),
        ("United Federation of Planets", "Klingon Empire", 87),
        ("United Federation of Planets", "Romulan Empire", 53),
        ("Bajoran", "Tholian Assembly", 80),
        ("Romulan Empire", "Borg", 33),
        ("Klingon Empire", "Borg", 41),
        ("Borg", "Tholian Assembly", 10)
    ] 
    for v1,v2,weight in edges:
        graph.add_edge(v1,v2,weight)


    # graph.add_edge("Cardassian Union", "Romulan Empire", 42)
    # graph.add_edge("Cardassian Union", "Bajoran", 14)
    # graph.add_edge("United Federation of Planets", "Bajoran", 22)
    # graph.add_edge("United Federation of Planets", "Klingon Empire", 87)
    # graph.add_edge("United Federation of Planets", "Romulan Empire", 53)
    # graph.add_edge("Bajoran", "Tholian Assembly", 80)
    # graph.add_edge("Romulan Empire", "Borg", 33)
    # graph.add_edge("Klingon Empire", "Borg", 41)
    # graph.add_edge("Borg", "Tholian Assembly", 10)

    # graph.display()
    print("Adjacency list:")
    graph.display()
    print("BFS from Bajoran: ", graph.bfs("Bajoran"))
    print("DFS from Bajoran: ", graph.dfs("Bajoran")) 

if __name__ =="__main__":
    main() 
    


# holyC

# terry davis 

