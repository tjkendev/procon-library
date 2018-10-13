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
 
 
# insert node with key = val and priority = pri
root = None
def insert(val, pri):
    global root
    st = []
    dr = []
    x = root
    while x:
        st.append(x)
        if x[2] == val:
            return
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
        root = nd
 
    for x in st:
        x[4] += 1
 
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
 
# delete node with key = val
def delete(val):
    global root
    x = root
 
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
    else:
        root = __delete(x)
 
# find node with key = val
def find(val):
    x = root
    while x:
        if val == x[2]:
            return 1
        x = x[x[2] < val]
    return 0