class RadixHeap:
    __slots__ = ["data", "last", "siz", "used"]

    # (max_key - min_key) <= C
    def __init__(self, N, C):
        self.data = [[] for i in range(C.bit_length() + 1)]
        self.last = self.siz = 0
        self.used = [0]*N

    def push(self, x, key):
        #assert self.last <= x
        self.siz += 1
        self.data[(x ^ self.last).bit_length()].append((x, key))

    def pop(self):
        data = self.data
        used = self.used
        #assert self.siz > 0
        if not data[0]:
            i = 1
            while not data[i]:
                i += 1
            d = data[i]
            new_last, new_key = min(d)
            used[new_key] = 1
            for val in d:
                x, key = val
                if used[key]:
                    self.siz -= 1
                    continue
                data[(x ^ new_last).bit_length()].append(val)
            self.last = new_last
            data[i] = []
        else:
            new_last, new_key = data[0].pop()
            used[new_key] = 1
            self.siz -= 1
        return new_last, new_key

    def __len__(self):
        return self.siz

def dijkstra(N, G, s):
    que = RadixHeap(N, 10**9 + 1)

    dist = [10**18]*N
    dist[s] = 0
    que.push(0, s)
    while que:
        cost, v = que.pop()
        if dist[v] < cost:
            continue
        for w, c in G[v]:
            if cost + c < dist[w]:
                dist[w] = r = cost + c
                que.push(r, w)
    return dist
