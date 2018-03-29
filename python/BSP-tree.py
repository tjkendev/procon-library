# kd-tree
# 入力: [(x, y), ...]
# 出力: kd-treeを保持するデータ
def kdTree(P):
    # [l, r)
    def make(l, r, depth):
        if r <= l+1:
            if l+1 == r:
                return [P[l], None, None]
            return None
        axis = depth % 2

        if r - l >= 3:
            M = len(P)
            med = l + (r-l)//2
            a0, a1, a2 = P[med-1:med+2]
            if a0 <= a1 <= a2:
                median = med
            elif a1 <= a0 <= a2:
                median = med-1
            else:
                median = med+1

            pivot = P[median][axis]
            s = l; t = r-1
            while s < t:
                while s < t and P[s][axis] <= pivot:
                    s += 1
                while s < t and pivot < P[t][axis]:
                    t -= 1
                P[s], P[t] = P[t], P[s]
            if s == r-1:
                median = s
            else:
                median = s-1
        else:
            median = l

        lc = make(l, median, depth+1)
        rc = make(median+1, r, depth+1)
        return [P[median], lc, rc]
    return make(0, len(P), 0)

def __search(node, q, d, depth):
    if node == None:
        return d
    p = node[0]
    dist = (p[0] - q[0])**2 + (p[1] - q[1])**2
    if dist < d:
        d = dist
    axis = depth % 2
    r = 1 if q[axis] < p[axis] else 2
    d = __search(node[r], q, d, depth+1)

    diff = abs(p[axis] - q[axis])
    if diff < d:
        d = __search(node[3-r], q, d, depth+1)
    return d

INF = 10**20
# 最近傍点の計算
# 入力: <tree>: kd-treeのデータ, <q>: (x, y)
def search(tree, q):
    return __search(tree, q, INF, 0)
