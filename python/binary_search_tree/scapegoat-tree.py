from math import log as log2
alpha = 0.7
beta = 1/log2(1/alpha)
 
# get the size of a tree t
def size(t):
    return size(t[0]) + size(t[1]) + 1 if t else 0
 
# rebuild a tree t
def __rebuild(t):
    res = []
    append = res.append
 
    def dfs(nd):
        nd[0] and dfs(nd[0])
        nd[4] and append(nd)
        nd[1] and dfs(nd[1])
    dfs(t)
 
    it = iter(res)
 
    def dfs0(p):
        if p == 1:
            nd = next(it)
            nd[0] = nd[1] = None
            nd[3] = 1
            return nd, 1
 
        l = None; lc = rc = 0
        m = p >> 1
        if m:
            l, lc = dfs0(m)
        nd = next(it)
        if m < p-1:
            nd[1], rc = dfs0(p-m-1)
        else:
            nd[1] = None
        nd[0] = l
        nd[3] = cc = lc + 1 + rc
        return nd, cc
    if not res:
        return None, 0
    return dfs0(len(res))

# find a node with key = val in a tree T
def find(T, val):
    x = T[0]
    while x and x[2] != val:
        x = x[x[2] < val]
    return x is not None

# insert a node with key = val into a tree T
def insert(T, val):
    st = []; dr = []
    t, M = T
    x = t; y = None
    while x and x[2] != val:
        y = x; d = (x[2] < val)
        st.append(y); dr.append(d)
        x = x[d]
    if x:
        if not x[4]:
            x[4] = 1
            x[3] += 1
            for z in st:
                z[3] += 1
        return t, M
 
    # [<left>, <right>, <key>, <count>, <is_exist>]
    nd = [None, None, val, 1, 1]
    if not y:
        return nd, 1
    y[d] = nd
 
    for z in st:
        z[3] += 1
 
    dpt = len(st) + 1
 
    if dpt > beta * log2(M):
        ct = nt = 1
        while st:
            y = st.pop(); d = dr.pop()
            nt = ct + 1 + size(y[d ^ 1])
            if alpha * nt < ct:
                break
            ct = nt
        if not st:
            return __rebuild(y)
        z = st.pop(); d = dr.pop()
        v, cc = __rebuild(y)
        z[d] = v
        return t, M-nt+cc
    return t, M+1
 
# delete a node with key = val from a tree T
def delete(T, val):
    t, M = T
    st = []; dr = []
    x = t; y = None
    while x and x[2] != val:
        y = x; d = (x[2] <= val)
        st.append(y); dr.append(d)
        x = x[d]
    if not x or not x[4]:
        return t, M
    x[4] = 0
    x[3] -= 1
    for z in st:
        z[3] -= 1
    if t[3] <= alpha * M:
        return __rebuild(t)
    return t, M