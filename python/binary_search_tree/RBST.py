import random
random.seed()
randint = random.randint

# merge tree l with tree r
def merge(l, r):
    if not l or not r:
        return l or r

    #st = []; dr = []
    z = y = [None]; d = 0
    while l and r:
        lc = l[3]; rc = r[3]
        if randint(1, lc+rc) <= lc:
            y[d] = l
            l[3] = lc+rc
            y = l; d = 1
            l = l[1]
        else:
            y[d] = r
            r[3] = lc+rc
            y = r; d = 0
            r = r[0]
        #st.append(y)
        #dr.append(d)
    y[d] = l or r
    #while st:
    #    x = st.pop(); d = dr.pop()
    return z[0]

# split a tree using stack info
def __split(st, dr):
    l = None; r = None
    st.reverse(); dr.reverse()
    for x, d in zip(st, dr):
        if d:
            x[1] = q = l
            p = x[0]
            l = x
        else:
            x[0] = p = r
            q = x[1]
            r = x
        x[3] = (p[3] if p else 0) + (q[3] if q else 0) + 1
    return l, r

# split tree t into two trees of size k and |t|-k
def split(t, k):
    if not t:
        return None, None
    x = t
    st = []; dr = []
    while x:
        l = x[0]
        c = (l[3] if l else 0) + 1

        st.append(x)
        if c <= k:
            k -= c
            x = x[1]
            d = 1
        else:
            x = x[0]
            d = 0
        dr.append(d)
    return __split(st, dr)

# insert a node with key = val
def insert(t, val):
    x = t
    st = []; dr = []
    while x:
        st.append(x)
        if x[2] == val:
            return t
        d = (x[2] < val)
        dr.append(d)
        x = x[d]

    l, r = __split(st, dr)

    # [<left>, <right>, <key>, <count>]
    nd = [None, None, val, 1]

    # merge tree l and node nd
    x = l; y = None
    while x:
        if not randint(0, x[3]):
            if y:
                y[1] = nd
            else:
                l = nd
            nd[0] = x
            nd[3] = x[3]+1
            break
        y = x
        x[3] += 1
        x = x[1]
    else:
        if y:
            y[1] = nd
        else:
            l = nd
    return merge(l, r)

# delete a node with key = val
def delete(t, val):
    x = t
    st = []; dr = []
    y = None
    while x:
        st.append(x)
        d = x[2] <= val
        dr.append(d)
        x = x[d]
    l, r = __split(st, dr)

    st = []; dr = []
    x = l
    while x:
        st.append(x)
        d = (x[2] < val)
        dr.append(d)
        x = x[d]
    l, m = __split(st, dr)

    #assert m[2] == val

    return merge(l, r)
