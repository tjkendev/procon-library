# Chu-Liu/Edmonds' Algorithm
# 最小全域有向木を再帰的に求める
# V: 頂点数, es: 辺集合, r: 根となる頂点番号
# 辺１つ(s->tのコストw)は(s, t, w)のlistを持つ
# 頂点は0..V-1
def solve(V, es, r):
    mins = [(10**18, -1)]*V
    for s, t, w in es:
        mins[t] = min(mins[t], (w, s))
    mins[r] = (-1, -1)

    group = [0]*V
    comp = [0]*V
    cnt = 0

    used = [0]*V
    for v in range(V):
        if not used[v]:
            chain = []
            cur = v
            while cur!=-1 and not used[cur]:
                chain.append(cur)
                used[cur] = 1
                cur = mins[cur][1]
            if cur!=-1:
                cycle = 0
                for e in chain:
                    group[e] = cnt
                    if e==cur:
                        cycle = 1
                        comp[cnt] = 1
                    if not cycle:
                        cnt += 1
                if cycle:
                    cnt += 1
            else:
                for e in chain:
                    group[e] = cnt
                    cnt += 1

    if cnt == V:
        return sum(map(lambda x:x[0], mins)) + 1

    res = sum(mins[v][0] for v in range(V) if v!=r and comp[group[v]])

    n_es = []
    for s, t, w in es:
        gs = group[s]; gt = group[t]
        if gs == gt:
            continue
        if comp[gt]:
            n_es.append((gs, gt, w - mins[t][0]))
        else:
            n_es.append((gs, gt, w))
    return res + solve(cnt, n_es, group[r])
