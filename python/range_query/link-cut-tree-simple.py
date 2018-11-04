N = 10**5

# prt[i]: 頂点iの親頂点
# left[i]: 頂点iの左部分木, right[i]: 頂点iの右部分木
# sz[i]: 頂点iを根頂点とする部分木のサイズ
# key[i]: 頂点iが持つ値
# val[i]: 頂点i以下の部分木の持つ値の和
prt = [0]*(N+1)
left = [0]*(N+1)
right = [0]*(N+1)
sz = [0] + [1]*N
key = [0]*(N+1)
val = [0]*(N+1)
 
def update(i, l, r):
    #assert 1 <= i <= N
    sz[i] = 1 + sz[l] + sz[r]
    val[i] = key[i] + val[l] + val[r]
 
def splay(i):
    #assert 1 <= i <= N
    q = prt[i]
    li = left[i]; ri = right[i]
    while q and not left[q] != i != right[q]:
        r = prt[q]
        if not r or left[r] != q != right[r]:
            y = r
            if left[q] == i:
                left[q] = ri
                if ri:
                    prt[ri] = q
                update(q, ri, right[q])
                ri = q; prt[q] = i
                update(i, li, q)
            else:
                right[q] = li
                if li:
                    prt[li] = q
                update(q, left[q], li)
                li = q; prt[q] = i
                update(i, q, ri)
        else:
            y = prt[r]
            if left[r] == q:
                if left[q] == i:
                    v = left[r] = right[q]
                    if v:
                        prt[v] = r
                    update(r, v, right[r])
 
                    left[q] = ri
                    if ri:
                        prt[ri] = q
                    update(q, ri, r)
 
                    right[q] = r; prt[r] = ri = q; prt[q] = i
                    update(i, li, q)
                else:
                    left[r] = ri
                    if ri:
                        prt[ri] = r
                    update(r, ri, right[r])
 
                    right[q] = li
                    if li:
                        prt[li] = q
                    update(q, left[q], li)
 
                    ri = r; li = q; prt[q] = prt[r] = i
                    update(i, q, r)
            else:
                if right[q] == i:
                    v = right[r] = left[q]
                    if v:
                        prt[v] = r
                    update(r, left[r], v)
 
                    right[q] = li
                    if li:
                        prt[li] = q
                    update(q, r, li)
 
                    left[q] = r; prt[r] = li = q; prt[q] = i
                    update(i, q, ri)
                else:
                    right[r] = li
                    if li:
                        prt[li] = r
                    update(r, left[r], li)
 
                    left[q] = ri
                    if ri:
                        prt[ri] = q
                    update(q, ri, right[q])
 
                    li = r; ri = q; prt[q] = prt[r] = i
                    update(i, r, q)
 
        if y:
            if left[y] == r:
                left[y] = i
                update(y, i, right[y])
            elif right[y] == r:
                right[y] = i
                update(y, left[y], i)
        q = y
    left[i] = li; right[i] = ri
    prt[i] = q
 
def expose(i):
    p = 0
    cur = i
    while cur:
        splay(cur)
        right[cur] = p
        update(cur, left[cur], p)
        p = cur
        cur = prt[cur]
    splay(i)
    return i
 
def cut(i):
    expose(i)
    p = left[i]
    left[i] = prt[p] = 0
    return p
 
def link(i, p):
    expose(i)
    expose(p)
    prt[i] = p
    right[p] = i