class Vertex:
    def __init__(self, node):
        self.id = node
        self.cons = {}
    
    def add_con(self, con, weight):
        self.cons[con] = weight
    
    def get_cons(self):
        return self.cons.keys()
    
    def get_id(self):
        return self.id

    def get_weight(self, con):
        return self.cons[con]

class Graph:
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, node):
        self.verticies[node] = Vertex(node)
        return self.verticies[node]

    def add_edge(self, frm, to, weight):
        if frm not in self.verticies:
            self.add_edge(frm)
        if to not in self.verticies:
            self.add_edge(to)

        self.verticies[frm].add_con(self.verticies[to], weight)
        self.verticies[to].add_con(self.verticies[frm], weight)

    def get_verticies(self):
        return self.verticies.keys()