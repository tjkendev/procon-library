def maximum_matching(N, G):
    def find_aug_path(N, G, M):
        que = []
        R = [-1]*N
        nxt = [-1]*N
        roots = [-1]*N
        valid = [1]*N

        for v in range(N):
            if M[v] != -1:
                continue
            que.append(v)
            roots[v] = v
            R[v] = 0

        for v in que:
            for w in G[v]:
                if w == M[v]:
                    continue
                if R[w] == -1:
                    x = M[w]

                    R[w] = 1
                    R[x] = 0

                    nxt[x] = v

                    roots[w] = roots[x] = roots[v]

                    que.append(x)
                elif R[w] == 0:
                    if roots[v] != roots[w]:
                        # construct an augmenting path
                        res = [v]
                        x = v
                        while M[x] != -1:
                            res.append(M[x])
                            x = nxt[x]
                            res.append(x)
                        res.reverse()
                        res.append(w)
                        x = w
                        while M[x] != -1:
                            res.append(M[x])
                            x = nxt[x]
                            res.append(x)
                        return res

                    # contract a blossom

                    P1 = [v]
                    x = v
                    while M[x] != -1:
                        x = nxt[x]
                        P1.append(x)
                    R1 = [x for x in reversed(P1) if valid[x]]

                    P2 = [w]
                    x = w
                    while M[x] != -1:
                        x = nxt[x]
                        P2.append(x)
                    R2 = [x for x in reversed(P2) if valid[x]]

                    ln = min(len(R1), len(R2))
                    k = 0
                    while k < ln and R1[k] == R2[k]:
                        k += 1

                    if k < len(R1):
                        u = R1[k]
                        py = w
                        for x in P1:
                            y = M[x]

                            if R[y] == 1:
                                que.append(y)
                                R[y] = 0
                            nxt[y] = py
                            valid[x] = valid[y] = 0

                            if x == u:
                                break
                            py = y

                    if k < len(R2):
                        u = R2[k]
                        py = v
                        for x in P2:
                            y = M[x]

                            if R[y] == 1:
                                que.append(y)
                                R[y] = 0
                            nxt[y] = py
                            valid[x] = valid[y] = 0

                            if x == u:
                                break
                            py = y
        return []
    M = [-1]*N
    while 1:
        P = find_aug_path(N, G, M)
        if not P:
            break
        for i in range(0, len(P), 2):
            p0 = P[i]; p1 = P[i+1]
            M[p0] = p1
            M[p1] = p0
    return M

N = 5
G = [[1], [0, 3, 4], [3], [1, 2, 4], [1, 3]]
M = maximum_matching(N, G)
print(M)
# => "[1, 0, 3, 2, -1]"