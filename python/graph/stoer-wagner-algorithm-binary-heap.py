from heapq import heapify
class BinaryHeap:
    def __init__(self):
        self.root = None
        self.mp = {}

    # build a heap: O(N)
    def build(self, A):
        A = [(v, k) for k, v in A]
        heapify(A)
        L = len(A)
        # node: [left, right, parent, key, id]
        mp = self.mp
        nds = [[None, None, None, v, k] for v, k in A]
        for i, nd in enumerate(nds):
            nd = nds[i]
            if 2*i+1 < L:
                nd[0] = nds[2*i + 1]
            if 2*i+2 < L:
                nd[1] = nds[i+i + 2]
            if i:
                nd[2] = nds[(i - 1) >> 1]
            mp[nd[4]] = nd
        self.root = nds[0]

    # decrease key: O(\log N)
    def decreasekey(self, k, d):
        node = self.mp[k]
        new_key = node[3] - d
        while node[2] and new_key < node[2][3]:
            node[3] = node[2][3]
            p_id = node[4] = node[2][4]
            self.mp[p_id] = node
            node = node[2]
        node[3] = new_key
        node[4] = k
        self.mp[k] = node

    # pop an item: O(\log N)
    def pop(self):
        target = cur = self.root
        v, k = target[3:5]
        while cur[0] and cur[1]:
            nxt = cur[0] if cur[0][3] < cur[1][3] else cur[1]
            cur[3:5] = nxt[3:5]
            self.mp[cur[4]] = cur
            cur = nxt
        nxt = cur[0] or cur[1]
        if self.root is cur:
            self.root = nxt
            if nxt:
                nxt[2] = None
        else:
            prt = cur[2]
            if prt[0] is cur:
                prt[0] = nxt
            else:
                prt[1] = nxt
            if nxt:
                nxt[2] = prt
        del self.mp[k]
        return k, v

    def empty(self):
        return self.root is None

def global_minimum_cut(N, G0, u0):
    res = 10**18

    G = [{w: d for w, d in G0[v]} for v in range(N)]

    merged = [0]*N
    while 1:
        # minimum cut phase
        used = [0]*N
        used[u0] = 1
        heap = BinaryHeap()

        data = []
        for v in range(N):
            if merged[v] or v == u0:
                continue
            data.append((v, -G[u0].get(v, 0)))
        heap.build(data)

        order = []
        while not heap.empty():
            v, _ = heap.pop()
            for w, d in G[v].items():
                if used[w]:
                    continue
                heap.decreasekey(w, d)
            used[v] = 1
            order.append(v)

        v = order[-1]
        ws = 0
        for w, d in G[v].items():
            ws += d
        res = min(res, ws)

        if len(order) == 1:
            break

        u = order[-2]

        # merge u and v
        merged[v] = 1
        for w, d in G[v].items():
            if w != u:
                if w in G[u]:
                    G[u][w] += d
                    G[w][u] += d
                else:
                    G[u][w] = G[w][u] = d
            del G[w][v]
        G[v] = None
    return res

N = 8
es = [
    (0, 1, 2),
    (1, 2, 3),
    (2, 3, 4),
    (0, 4, 3),
    (1, 4, 2),
    (1, 5, 2),
    (2, 6, 2),
    (3, 6, 2),
    (3, 7, 2),
    (4, 5, 3),
    (5, 6, 1),
    (6, 7, 3),
]
G = [[] for i in range(N)]
for a, b, w in es:
    G[a].append((b, w))
    G[b].append((a, w))
print(global_minimum_cut(N, G, 1))
# => "4"
