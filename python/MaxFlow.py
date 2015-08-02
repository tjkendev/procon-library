# Ford-Fulkerson algorithm
class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.g = [[] for i in xrange(n)]
    def add_edge(self, fr, to, cap):
        self.g[fr].append([to, cap, len(self.g[to])])
        self.g[to].append([fr, 0, len(self.g[fr])-1])
    def add_multi_edge(self, v1, v2, cap1, cap2):
        self.g[v1].append([v2, cap1, len(self.g[v2])])
        self.g[v2].append([v1, cap2, len(self.g[v1])-1])
    def dfs(self, v, t, f):
        if v==t: return f
        used = self.used
        used[v] = True
        for e in self.g[v]:
            if not used[e[0]] and e[1]>0:
                d = self.dfs(e[0], t, min(f, e[1]))
                if d>0:
                    e[1] -= d
                    self.g[e[0]][e[2]][1] += d
                    return d
        return 0
    def max_flow(self, s, t):
        flow = 0
        while True:
            self.used = [0]*self.n
            f = self.dfs(s, t, 10**9+7)
            if f==0: break
            flow += f
        return flow
# Dinic algorithm
import Queue
class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for i in xrange(n)]
    def add_edge(self, fr, to, cap):
        self.g[fr].append([to, cap, len(self.g[to])])
        self.g[to].append([fr, 0, len(self.g[fr])-1])
    def add_multi_edge(self, v1, v2, cap1, cap2):
        self.g[v1].append([v2, cap1, len(self.g[v2])])
        self.g[v2].append([v1, cap2, len(self.g[v1])-1])
    def bfs(self, s):
        level = [-1]*self.n
        que = Queue.Queue()
        level[s] = 0
        que.put(s)
        while not que.empty():
            v = que.get()
            for e in self.g[v]:
                if e[1]>0 and level[e[0]]<0:
                    level[e[0]] = level[v] + 1
                    que.put(e[0])
        self.level = level
    def dfs(self, v, t, f):
        if v==t: return f
        es = self.g[v]
        level = self.level
        for i in xrange(self.it[v], len(self.g[v])):
            e = es[i]
            if e[1]>0 and level[v]<level[e[0]]:
                d = self.dfs(e[0], t, min(f, e[1]))
                if d>0:
                    e[1] -= d
                    self.g[e[0]][e[2]][1] += d
                    self.it[v] = i
                    return d
        self.it[v] = len(self.g[v])
        return 0
    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t]<0: break
            self.it = [0]*self.n
            while True:
                f = self.dfs(s, t, 10**9+7)
                if f>0:
                    flow += f
                else:
                    break
        return flow
