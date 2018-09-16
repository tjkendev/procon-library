# 2部グラフ - 最小辺カバー (bipartite graph - minimum edge cover)
# 1. 最大流を行う
# 2. 使われていない点を数える
class MinEdgeCover:
    def __init__(self, a, b):
        self.dinic = dinic = Dinic(2+a+b)
        self.a = a; self.b = b
        self.fm = fm = {}; self.tm = tm = {}
        for i in range(a):
            dinic.add_edge(0, 2+i, 1)
            fm[i] = dinic.g[0][-1]
        for i in range(b):
            dinic.add_edge(2+a+i, 1, 1)
            tm[i] = dinic.g[2+a+i][-1]
    def add_edge(self, f, t):
        self.dinic.add_edge(2+f, 2+self.a+t, 1)
    def min_edge_cover(self):
        flow = self.dinic.max_flow(0, 1)
        for i in range(self.a):
            cap = self.fm[i][1]
            if cap>0:
                flow += 1
        for i in range(self.b):
            cap = self.tm[i][1]
            if cap>0:
                flow += 1
        return flow

