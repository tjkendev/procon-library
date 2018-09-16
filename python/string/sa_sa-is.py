# SA-IS (O(nlogn))
from collections import Counter
def SAIS(lst, num):
    l = len(lst)
    if l<2: return lst+[0]
    lst = lst + [0]
    l += 1
    res = [None] * l
    t = [1] * l
    for i in range(l-2, -1, -1):
        t[i] = 1 if lst[i]<lst[i+1] or (lst[i]==lst[i+1] and t[i+1]) else 0
    isLMS = [t[i-1]<t[i] for i in range(l)]
    LMS = [i for i in range(1, l) if t[i-1]<t[i]]
    LMSn = len(LMS)

    cbase = Counter(lst)
    count = cbase.copy()
    tmp = 0
    cstart = [0]*(num+1); cend = [0]*(num+1)
    for key in range(num+1):
        cstart[key] = tmp
        count[key] += tmp
        cend[key] = tmp = count[key]

    for e in reversed(LMS):
        count[lst[e]] -= 1
        res[count[lst[e]]] = e

    for e in res:
        if e>0 and not t[e-1]:
            res[cstart[lst[e-1]]] = e-1
            cstart[lst[e-1]] += 1
    for e in reversed(res):
        if e>0 and t[e-1]:
            cend[lst[e-1]] -= 1
            res[cend[lst[e-1]]] = e-1

    name = 0; prev = -1
    pLMS = {}
    for e in res:
        if isLMS[e]:
            for i in range(l):
                if prev==-1 or lst[e+i]!=lst[prev+i]:
                    name += 1; prev = e
                    break
                elif i and (isLMS[e+i] or isLMS[prev+i]): break
            pLMS[e] = name-1

    if name < LMSn:
        sublst = [pLMS[e] for e in LMS if e<l-1]
        ret = SAIS(sublst, name-1)

        LMS = map(LMS.__getitem__, reversed(ret))
    else:
        LMS = [e for e in reversed(res) if isLMS[e]]

    res = [None]*l
    count = cbase
    tmp = 0
    for key in range(num+1):
        cstart[key] = tmp
        count[key] += tmp
        cend[key] = tmp = count[key]

    for e in LMS:
        count[lst[e]] -= 1
        res[count[lst[e]]] = e

    for e in res:
        if e and not t[e-1]:
            res[cstart[lst[e-1]]] = e-1
            cstart[lst[e-1]] += 1
    for e in reversed(res):
        if e and t[e-1]:
            cend[lst[e-1]] -= 1
            res[cend[lst[e-1]]] = e-1

    return res
def chr_compression(s):
    uniq = list(set(s))
    uniq.sort()
    return map({e: i+1 for i, e in enumerate(uniq)}.__getitem__, s), len(uniq)
# usage: SAIS(*chr_compression(<string>))

def LCP(s, n, sa):
    lcp = [-1]*(n+1)
    rank = [0]*(n+1)
    for i in range(n+1): rank[sa[i]] = i

    h = 0
    lcp[0] = 0
    for i in range(n):
        j = sa[rank[i] - 1]
        if h > 0: h -= 1
        while j+h < n and i+h < n and s[j+h]==s[i+h]:
            h += 1
        lcp[rank[i] - 1] = h
    return lcp
