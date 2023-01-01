# set()のような要素の追加削除 + lower_bound() を実現するセグ木
# 追加削除される要素が先読みできる場合に利用可
E = [1, 10, 15] # 追加削除される要素のリスト (sorted)
mp = {e: i for i, e in enumerate(E)}

# 区間[L, R] := 区間[E[L], E[R]]に存在する最大要素 (なければNone)
L = len(E)
L0 = 2**(L-1).bit_length()
data = [None]*(L0*2)
# 要素eをx個追加: O(logN)
def update(e, x):
    k = mp[e]
    k += L0 - 1
    if data[k] is None:
        r = data[k] = [e, x]
    else:
        r = data[k]
        r[1] = max(0, r[1]+x)
    while k:
        k = (k - 1) // 2
        l = data[2*k+1]; r = data[2*k+2]
        if r and r[1]:
            if data[k] is r:
                return
            data[k] = r
        elif l and l[1]:
            if data[k] is l:
                return
            data[k] = l
        else:
            if data[k] is None:
                return
            data[k] = None
# v以上の要素を二分探索により検索: O(logN)
def lower_bound(v):
    f = data[0]
    if not f or f[0] < v or f[1] == 0:
        return None
    k = 0
    while k < L0 - 1:
        l = data[2*k+1]
        if l is None or l[1] == 0 or l[0] < v:
            k = 2*k+2
        else:
            k = 2*k+1
    #assert data[k][1] > 0
    return E[k - (L0 - 1)]
# 含有判定: O(1)
def contain(v):
    k = mp[v]
    r = data[k + L0 - 1]
    return r and r[1] > 0
