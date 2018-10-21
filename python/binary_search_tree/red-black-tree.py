# rotate a tree nd
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

    r = c[3] = nd[3]
    nd[3] = r - (e[3] if e else 0) - 1
    return c

# insert a node with key = val into a tree t
def insert(t, val):
    x = t
    st = []; dr = []
    y = None
    while x:
        y = x
        st.append(x)
        if x[2] == val:
            return t
        d = (x[2] < val)
        dr.append(d)
        x = x[d]

    # [<left>, <right>, <key>, <count>, <color: [BLACK,RED]>]
    nd = [None, None, val, 1, 1]

    if not y:
        nd[4] = 0
        return nd

    y[d] = nd
    for x in st:
        x[3] += 1

    while 1:
        if not st:
            # if nd is the root node
            nd[4] = 0
            return nd

        # nd's parent
        y = st.pop(); dy = dr.pop()
        if not y[4]:
            # if nd's parent is black
            return t

        # nd's grandparent
        w = st.pop(); dw = dr.pop()
        # nd's uncle
        z = w[dw ^ 1]
        if z and z[4]:
            # the parent and the uncle is red
            y[4] = z[4] = 0
            w[4] = 1
            nd = w
            continue

        if dw != dy:
            w[dw] = rotate(y, dy)
            nd, y = y, nd

        rotate(w, dw)
        y[4] = 0
        w[4] = 1

        if st:
            st[-1][dr[-1]] = y
            return t
        return y

# delete a node nd
def __delete(st, dr, nd):
    x = nd
    if x[0]:
        st.append(x); dr.append(0)
        x = x[0]
        while x:
            st.append(x); dr.append(1)
            x = x[1]

        y = st.pop(); dr.pop()
        # copy a value only
        nd[2] = y[2]
    elif x[1]:
        st.append(x); dr.append(1)
        x = x[1]
        while x:
            st.append(x); dr.append(0)
            x = x[0]

        y = st.pop(); dr.pop()
        # copy a value only
        nd[2] = y[2]
    else:
        y = nd

    # delete the node (y) with at most one non-leaf child
    for x in st:
        x[3] -= 1

    c = y[0] if y[0] else y[1]
    if st:
        st[-1][dr[-1]] = c

    if y[4]:
        # if nd is red
        return st[0] if st else c

    if c and c[4]:
        # if nd is black and child is red
        c[4] = 0
        return st[0] if st else c

    # nd and child is black: delete in each cases

    n = c
    while st:
        p = st.pop(); dp = dr.pop()
        # n's sibling
        s = p[dp ^ 1]
        #assert s
        sc = s[dp]; sd = s[dp ^ 1]

        if s[4]:
            #assert sc and sd
            p[4] = 1; s[4] = 0
            if st:
                st[-1][dr[-1]] = rotate(p, dp ^ 1)
            else:
                rotate(p, dp ^ 1)
            st.append(s); dr.append(dp)
            #assert p[dp ^ 1] is sc
            s = sc
            sc = s[dp]; sd = s[dp ^ 1]
            break

        if p[4] or (sc and sc[4]) or (sd and sd[4]):
            break

        s[4] = 1
        n = p
    else:
        return n

    if p[4] and not s[4] and not (sc and sc[4]) and not (sd and sd[4]):
        p[4] = 0; s[4] = 1
        return st[0] if st else p

    sc = s[dp]; sd = s[dp ^ 1]
    if not s[4] and (sc and sc[4]) and not (sd and sd[4]):
        sc[4] = 0; s[4] = 1
        sd = s
        s = p[dp ^ 1] = rotate(s, dp)

    #assert not s[4] and (sd and sd[4])
    s[4] = p[4]
    p[4] = 0
    sd[4] = 0

    if st:
        st[-1][dr[-1]] = rotate(p, dp ^ 1)
    else:
        return rotate(p, dp ^ 1)

    return st[0] if st else n

# delete a node with key = val from a tree t
def delete(t, val):
    x = t

    st = []; dr = []
    while x and val != x[2]:
        d = (x[2] < val)
        st.append(x); dr.append(d)
        x = x[d]
    if not x:
        return t
    # x is the node with key = val
    return __delete(st, dr, x)
