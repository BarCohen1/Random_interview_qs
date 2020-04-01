# BFS

from queue import Queue


class Vertex:
    def __init__(self):
        self.visited = False
        self.parent = None
        self.neighbors = []
        self.disc = 0
        self.finished = 0


class G:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.start = V[0]
        self.time = 0

    def findPath(self, v:Vertex):
        if v == self.start:
            return [v]
        if not v.parent:
            return None
        self.findPath(v.parent).append(v)

    def reset_G(self):
        for i in range(len(self.V)):
            self.V[i] = Vertex()
        for v, u in self.E:
            v.neighbors.add(u)

    def BFS(self):
        def RunBFS(start):
            q = Queue()
            q.put(start)
            while q.not_empty:
                cur_v = q.get()
                cur_v.visited = True
                for n in cur_v.neighbors:
                    if not n.visited:
                        n.parent = cur_v
                        q.put(n)

        self.reset_G()
        RunBFS(self.start)

    def DFS(self):
        def DFSV(v:Vertex):
            if not v.visited and v.disc < 0:
                v.disc = self.time + 1
                v.visited = True
                for n in v.neighbors:
                    n.parent = v
                    DFSV(n)
                v.finished = self.time +1
                self.time += 1
        self.reset_G()
        DFSV(self.start)