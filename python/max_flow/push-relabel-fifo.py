from collections import deque
class PushRelabel:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]
        self.initial = [N]*N
        self.zeros = [0]*(N+1)

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    # Global labeling
    def bfs(self, H, D, t, que=deque()):
        que.append(t)
        G = self.G
        H[:] = self.initial
        H[t] = 0
        D[:] = self.zeros
        D[0] = 1
        N = self.N
        c = N-1
        while que:
            v = que.popleft()
            d = H[v] + 1
            for w, cap, backward in G[v]:
                if H[w] <= d or backward[1] == 0:
                    continue
                H[w] = d
                D[d] += 1
                c -= 1
                que.append(w)
        D[N] = c
        return d # gap

    # FIFO preflow-push algorithm
    def flow(self, s, t):
        N = self.N
        H = [0]*N # height
        F = [0]*N # excess flow
        D = [0]*(N+1) # distance label
        active = [0]*N # active node

        G = self.G

        que = deque([s])
        F[s] = 10**18
        active[s] = 1

        gap = self.bfs(H, D, t)

        cnt = 0
        while que:
            v = que.popleft()
            if v == t:
                continue

            hv = H[v]
            # Gap-relabeling
            if hv > gap:
                D[hv] -= 1
                D[N] += 1
                hv = H[v] = N
                continue
            # push
            rest = F[v]
            for e in G[v]:
                w, cap, backward = e
                if cap and hv > H[w] < gap:
                    d = min(rest, cap)
                    e[1] -= d
                    backward[1] += d
                    rest -= d
                    F[w] += d
                    if not active[w]:
                        que.append(w)
                        active[w] = 1
                    if rest == 0:
                        break
            F[v] = rest

            if rest == 0:
                active[v] = 0
                continue

            # relabel
            h0 = H[v]
            hv = N
            for w, cap, backward in G[v]:
                if cap and hv > H[w] + 1 <= gap:
                    hv = H[w] + 1
            if hv != h0:
                D[h0] -= 1
                if D[h0] == 0 and h0 < gap:
                    gap = h0
                    hv = N
                elif hv == gap:
                    gap += 1
                D[hv] += 1

            H[v] = hv
            if hv < N:
                que.append(v)
            else:
                active[v] = 0

            cnt += 1
            if cnt % N == 0:
                gap = self.bfs(H, D, t)
        return F[t]