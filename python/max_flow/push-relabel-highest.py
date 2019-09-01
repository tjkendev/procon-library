from collections import deque
class PushRelabel:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]
        self.initial = [N]*N
        self.zeros = [0]*N

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
    def bfs(self, H, D, active, t, que=deque()):
        N = self.N
        B = [[] for i in range(N)]
        que.append(t)
        G = self.G
        H[:] = self.initial
        H[t] = 0
        D[:] = self.zeros
        D[0] = 1
        cur = 0
        while que:
            v = que.popleft()
            d = H[v] + 1
            for w, cap, backward in G[v]:
                if H[w] <= d or backward[1] == 0:
                    continue
                H[w] = d
                if active[w] and d < N:
                    B[d].append(w)
                    cur = d
                if d < N:
                    D[d] += 1
                que.append(w)
        return B, cur, d

    # Highest preflow-push algorithm
    def flow(self, s, t):
        N = self.N
        H = [0]*N # height
        F = [0]*N # excess flow
        D = [0]*(N+1) # distance label
        active = [0]*N # active node

        G = self.G

        F[s] = 10**18
        active[s] = 1

        B, cur, gap = self.bfs(H, D, active, t)
        B[cur].append(s)

        cnt = 0
        while 1:
            while cur >= 0 and not B[cur]:
                cur -= 1
            if cur < 0:
                break
            v = B[cur].pop()
            if v == t:
                continue

            hv = H[v]
            # Gap-relabeling
            if hv > gap:
                if hv < N:
                    D[hv] -= 1
                #D[N] += 1
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
                        hw = H[w]
                        B[hw].append(w)
                        if cur < hw:
                            cur = hw
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
            if h0 != hv:
                D[h0] -= 1
                if D[h0] == 0 and h0 < gap:
                    gap = h0
                    hv = N
                elif hv == gap:
                    gap += 1
                if hv < N:
                    D[hv] += 1

            H[v] = hv
            if hv < N:
                B[hv].append(v)
                if cur < hv:
                    cur = hv
            else:
                active[v] = 0

            cnt += 1
            if cnt % N == 0:
                B, cur, gap = self.bfs(H, D, active, t)
        return F[t]
