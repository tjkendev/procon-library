from collections import deque

def scc(N, G, RG):
    order = []
    used = [0]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    for i in range(N):
        if not used[i]:
            dfs(i)
    group = [-1]*N
    label = 0
    order.reverse()
    for s in order:
        if group[s] != -1:
            continue
        que = deque([s])
        group[s] = label
        while que:
            v = que.popleft()
            for w in RG[v]:
                if group[w] != -1:
                    continue
                que.append(w)
                group[w] = label
        label += 1
    return group # topological ordering

N = ...
G = [[] for i in range(2*N)]
RG = [[] for i in range(2*N)]
# add (a ∨ b)
# a =  x_i if neg_i = 0
# a = ~x_i if neg_i = 1
def add_edge(i, neg_i, j, neg_j):
    if neg_i:
        i0 = i+N; i1 = i
    else:
        i0 = i; i1 = i+N
    if neg_j:
        j0 = j+N; j1 = j
    else:
        j0 = j; j1 = j+N
    # add (~a ⇒ b)
    G[i1].append(j0); RG[j0].append(i1)
    # add (~b ⇒ a)
    G[j1].append(i0); RG[i0].append(j1)

group = scc(2*N, G, RG)

# check if the formula is satisfiable
def check(group):
    for i in range(N):
        if group[i] == group[i+N]:
            return False
    return True

# assign values to variables
def assign(group):
    res = [0]*N
    for i in range(N):
        if group[i] > group[i+N]:
            res[i] = 1
    return res