# splay a node nd
def __splay(st, dr, nd):
    l = nd[0]; r = nd[1]
    L = (l[3] if l else 0); R = (r[3] if r else 0)
    c = len(st) >> 1
    while c:
        # y(d1)-x(d)-nd
        x = st.pop(); y = st.pop()
        d = dr.pop(); d1 = dr.pop()

        if d == d1:
            # Zig-zig step
            y[3] = e = y[3] - L - R - 2
            if d:
                y[1] = x[0]; x[0] = y
                x[1] = l; l = x

                l[3] = L = e + L + 1
            else:
                y[0] = x[1]; x[1] = y
                x[0] = r; r = x

                r[3] = R = e + R + 1
        else:
            # Zig-zag step
            if d:
                x[1] = l; l = x
                y[0] = r; r = y

                l[3] = L = l[3] - R - 1
                r[3] = R = r[3] - L - 1
            else:
                x[0] = r; r = x
                y[1] = l; l = y

                r[3] = R = r[3] - L - 1
                l[3] = L = l[3] - R - 1
        c -= 1
        # update(y); update(x)
    if st:
        # Zig step
        x = st[0]; d = dr[0]
        if d:
            x[1] = l; l = x
            l[3] = L = l[3] - R - 1
        else:
            x[0] = r; r = x
            r[3] = R = r[3] - L - 1
        # update(x)
    nd[0] = l; nd[1] = r
    nd[3] = L + R + 1
    # update(nd)
    return nd

# create a new node with key = val
def new_node(val):
    return [None, None, val, 1]

# insert a node with key = val
def insert(t, val):
    # [<left>, <right>, <key>, <count>]
    nd = [None, None, val, 1]
    st = []; dr = []
    x = t; y = None
    while x:
        y = x; d = (x[2] <= val)
        st.append(y); dr.append(d)
        x[3] += 1
        x = x[d]

    if not y:
        return nd
    y[d] = nd
    return __splay(st, dr, nd)

# delete a node with key = val
def delete(t, val):
    st = []; dr = []
    x = t
    while x and x[2] != val:
        d = (x[2] <= val)
        st.append(x); dr.append(d)
        x = x[d]
    if not x:
        return t
    t = __splay(st, dr, x)
    return merge(t[0], t[1])

# find a node with key = val
def find(t, val):
    st = []; dr = []
    x = t
    while x and x[2] != val:
        d = (x[2] <= val)
        st.append(x); dr.append(d)
        x = x[d]
    if not x:
        return t, False
    t = __splay(st, dr, x)
    return t, True

# find k-th node in a tree t
def findk(t, k):
    if not t or not 0 < k <= t[3]:
        return t
    x = t
    st = []; dr = []
    while x:
        l = x[0]
        c = (l[3] if l else 0) + 1
 
        if c == k:
            break
 
        st.append(x)
        if c < k:
            k -= c
            x = x[1]
            dr.append(1)
        else:
            x = x[0]
            dr.append(0)
    return __splay(st, dr, x)

# merge a tree l with a tree r
def merge(l, r):
    if not l or not r:
        return l or r
    if not l[1]:
        l[3] += r[3]
        l[1] = r
        return l

    st = []
    x = l
    while x[1]:
        st.append(x)
        x = x[1]

    l = __splay(st, [1]*len(st), x)
    l[3] += r[3]
    l[1] = r
    # update(l)
    return l

# split a tree t into two trees of size k and |t|-k
def split(t, k):
    if not t:
        return None, None
    if not 0 < k < t[3]:
        if k == t[3]:
            return findk(t, k), None
        return None, t
    x = t
    st = []; dr = []
    while x:
        l = x[0]
        c = (l[3] if l else 0) + 1

        if c == k:
            break

        st.append(x)
        if c < k:
            k -= c
            x = x[1]
            dr.append(1)
        else:
            x = x[0]
            dr.append(0)
    l = __splay(st, dr, x)
    r = l[1]
    if r:
        l[3] -= r[3]
    l[1] = None
    # update(l)
    return l, r
