# Treap

# d = 0: right rotation
# d = 1: left rotation
def rotate(nd, d):
    c = nd[d]
    if d:
        e = c[1]
        nd[1] = c[0]
        c[0] = nd
    else:
        e = c[0]
        nd[0] = c[1]
        c[1] = nd

    r = c[4] = nd[4]
    nd[4] = r - (e[4] if e else 0) - 1
    return c

# insert a node with key = val and priority = pri
def insert(t, val, pri):
    st = []
    dr = []
    x = t
    while x:
        st.append(x)
        if x[2] == val:
            return t
        d = (x[2] < val)
        dr.append(d)
        x = x[d]

    # [<left>, <right>, <key>, <priority>, <count>]
    nd = [None, None, val, pri, 1]
    while st:
        x = st.pop(); d = dr.pop()
        x[d] = nd
        x[4] += 1
        if x[3] >= nd[3]:
            break
        rotate(x, d)
    else:
        return nd

    for x in st:
        x[4] += 1
    return t

# delete node nd
def __delete(nd):
    st = []; dr = []
    while nd[0] or nd[1]:
        l = nd[0]; r = nd[1]
        d = (l[3] <= r[3]) if l and r else (l is None)
        st.append(rotate(nd, d))
        dr.append(d ^ 1)
    nd = x = None
    while st:
        nd = x; x = st.pop(); d = dr.pop()
        x[d] = nd
        x[4] -= 1
    return x

# delete a node with key = val
def delete(t, val):
    x = t

    st = []
    y = None
    while x:
        if val == x[2]:
            break
        y = x; d = (x[2] < val)
        st.append(y)
        x = x[d]
    else:
        return

    if y:
        y[d] = __delete(x)
        for x in st:
            x[4] -= 1
        return t
    return __delete(x)

# find a node with key = val
def find(t, val):
    x = t
    while x:
        if val == x[2]:
            return 1
        x = x[x[2] < val]
    return 0

# merge tree l with tree r
def merge(l, r):
    if not l:
        return r
    if not r:
        return l
    nd = [l, r, None, None, l[4]+r[4]+1]
    return __delete(nd)

# split tree t into two trees of size k and |t|-k
def split(t, k):
    x = t
    if not 0 < k < x[4]:
        return t, None
    st = []; dr = []
    while x:
        l = x[0]

        c = (l[4] if l else 0) + 1
        if c == k:
            break
        y = x
        st.append(y)

        if c < k:
            k -= c
            x = x[1]
            d = 1
        else:
            x = l
            d = 0
        dr.append(d)
    # x is k-th element in tree t
    #assert x
    st.append(x)
    dr.append(1)
    x = x[1]
    while x:
        st.append(x)
        dr.append(0)
        x = x[0]
    nd = [None, None, None, None, 1]
    while st:
        x = st.pop(); d = dr.pop()
        x[d] = nd
        x[4] += 1
        rotate(x, d)
    return nd[0], nd[1]

# for debug
def debug(t):
    def dfs(t, k):
        cc = 1
        if t[0]:
            cc += dfs(t[0], k+1)
        print(" "*k, "%d (%d) %d" % (t[2], t[3], t[4]))
        if t[1]:
            cc += t[1] and dfs(t[1], k+1)
        assert t[4] == cc
        return cc
    if not t:
        return 0
    return dfs(t, 0)
