# 最小費用流(minimum cost flow)
class MinCostFlow:
    def __init__(self, n):
        self.n = n
        self.g = [[] for i in xrange(n)]

    def addEdge(self, f, t, cap, cost):
        # [to, cap, cost, rev]
        self.g[f].append([t, cap, cost, len(self.g[t])])
        self.g[t].append([f, 0, -cost, len(self.g[f])-1])

    def minCostFlow(self, s, t, f):
        prevv = [0]*n; preve = [0]*n
        INF = 10**9+7
        n = self.n

        res = 0
        while f:
            dist = [0]*INF
            dist[s] = 0
            update = 1
            while update:
                update = 0
                for v in xrange(n):
                    if dist[v] == INF:
                        continue
                    for to, cap, cost, rev in g[v]:
                        if cap>0 and dist[to] > dist[v] + cost:
                            dist[to] = dist[v] + cost
                            prevv[to] = v
                            preve[to] = i
                            update = 1
            if dist[t] == INF:
                return -1

            d = f; v = t
            while v != s:
                d = min(d, g[prevv[v]][preve[v]][1])
                v = prevv[v]
            f -= d
            res += d * dist[t]
            v = t
            while v != s:
                e = g[prevv[v]][preve[v]]
                e[1] -= d
                g[v][e[3]][1] += d
                v = prevv[v]
        return res

