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

    def insert_sorted(self,vertex,neighbor,weight):
        neighbor_list = self.adj_list[vertex]
        new_edge = (neighbor, weight)

        #self.adj_list.push_back
        #existing_neighbor = self.neighbor_list - 1
        #existing_weight = self.new_edge(weight)
        for i, (existing_neighbor, existing_weight) in enumerate(neighbor_list):
            if existing_weight > weight:
                neighbor_list.insert(i, new_edge)
                return 
            neighbor_list.append(new_edge)
            


    def add_edge(self, v1,v2,weight):
        if not v1:
            print("v1 does not exist here")
            exit 
        if not v2:
            print("v2 does not exist")
            exit 
    insert_sorted(v2,v2,weight)     #v1's list gets (v2,weight)
    insert_sorted(v2,v1,weight)     #v2's list gets (v1,weight)


def main():
    _graph = Graph()

    factions = ["Cardassian Union", "United Federation of Planets","Bajoran","Romulan Empire","Kilngon EMpire","Borg","Tholian Assembly"]

    for f in factions:
        _graph.add_vertex(f)

    _graph.add_edge("Cardassian Union", "Romulan Empire", 42)
    _graph.add_edge("Cardassian Union", "Bajoran", 14)
    _graph.add_edge("United Federation of Planets", "Bajoran", 22)
    _graph.add_edge("United Federation of Planets", "Klingon Empire", 87)
    _graph.add_edge("United Federation of Planets", "Romulan Empire", 53)
    _graph.add_edge("Bajoran", "Tholian Assembly", 80)
    _graph.add_edge("Romulan Empire", "Borg", 33)
    _graph.add_edge("Klingon Empire", "Borg", 41)
    _graph.add_edge("Borg", "Tholian Assembly", 10)

if __name__ =="__main__":
    main() 
