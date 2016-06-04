#
# Suffix Array
#

# Manber & Myers : O(n(logn)^2)
class SuffixArray:
    def __init__(self, s):
        self.s = s
        self.n = len(s)

    # Suffix Array
    def suffix(self):
        s = self.s; n = self.n
        rank = [0]*(n+1); sa = [0]*(n+1)
        tmp = [0]*(n+1)

        for i in xrange(n+1):
            sa[i] = i
            rank[i] = ord(s[i]) if i<n else -1

        k = 1
        cmp_key = lambda e: (rank[e], rank[e+k] if e+k<=n else -1)
        while k <= n:
            sa.sort(key=cmp_key)
            tmp[sa[0]] = 0
            for i in xrange(1, n+1):
                tmp[sa[i]] = tmp[sa[i-1]] + (cmp_key(sa[i-1])<cmp_key(sa[i]))
            for i in xrange(n+1):
                rank[i] = tmp[i]
            k *= 2

        self.sa = sa
        return sa

    # LCP Array
    def lcp(self):
        n = self.n; s = self.s; sa = self.sa
        lcp = [-1]*(n+1)
        rank = [0]*(n+1)
        for i in xrange(n+1): rank[sa[i]] = i

        h = 0
        lcp[0] = 0
        for i in xrange(n):
            j = sa[rank[i] - 1]
            if h > 0: h -= 1
            while j+h < n and i+h < n and s[j+h]==s[i+h]:
                h += 1
            lcp[rank[i] - 1] = h
        self.lcp = lcp
        return lcp

# SA-IS (O(nlogn))
def SuffixArray(s):
    m = map(ord, s)
    m.append(-1)
    n = len(m)

    def i_large(t, SA, s, bktl):
        bkt = {}
        for k in bktl: bkt[k] = bktl[k]
        for e in SA:
            j = e-1
            if j>=0 and not t[j]:
                SA[bkt[s[j]]] = j
                bkt[s[j]] += 1

    def i_small(t, SA, s, bkts):
        bkt = {}
        for k in bkts: bkt[k] = bkts[k]
        for e in reversed(SA):
            j = e-1
            if j>=0 and t[j]:
                bkt[s[j]] -= 1
                SA[bkt[s[j]]] = j

    def SAIS(s, n):
        t = [0]*n; LMS = [0]*n
        SA = [0]*n

        t[-2] = 0; t[-1] = 1
        for i in xrange(n-3, -1, -1):
            t[i] = 1 if s[i]<s[i+1] or (s[i]==s[i+1] and t[i+1]) else 0
        for i in xrange(1, n):
            LMS[i] = 1 if t[i] and not t[i-1] else 0

        su = 0
        bkt = {}
        bktl = {}; bkts = {}
        for c in s: bkt[c] = bkt.get(c, 0) + 1
        for k in sorted(bkt):
            bktl[k] = su
            su += bkt[k]
            bkts[k] = su

        for k in bkts: bkt[k] = bkts[k]
        for i in xrange(n): SA[i] = -1
        for i in xrange(1, n):
            if LMS[i]:
                bkt[s[i]] -= 1
                SA[bkt[s[i]]] = i

        i_large(t, SA, s, bktl)
        i_small(t, SA, s, bkts)

        n1 = 0
        for e in SA:
            if e>0 and LMS[e]:
                SA[n1] = e
                n1 += 1

        for i in xrange(n1, n): SA[i] = -1
        cnt = 0; prev = -1
        for i in xrange(n1):
            pos = SA[i]
            for d in xrange(n):
                if prev==-1 or s[pos+d]!=s[prev+d] or t[pos+d]!=t[prev+d]:
                    cnt += 1
                    prev = pos
                    break
                elif LMS[pos+d] or LMS[prev+d]: break
            pos /= 2
            SA[n1+pos] = cnt-1
        j = n-1
        for i in xrange(n-1, n1-1, -1):
            if SA[i]>=0:
                SA[j] = SA[i]
                j -= 1

        if cnt<n1:
            SA[:n1] = SAIS(SA[-n1:], n1)
        else:
            for i in xrange(n1): SA[SA[i-n1]] = i

        for k in bkts: bkt[k] = bkts[k]
        j = 0
        for i in xrange(1, n):
            if LMS[i]:
                SA[j-n1] = i
                j += 1
        for i in xrange(n1): SA[i] = SA[SA[i]-n1]
        for i in xrange(n1, n): SA[i] = -1

        for i in xrange(n1-1, -1, -1):
            j = SA[i]; SA[i] = -1
            bkt[s[j]] -= 1
            SA[bkt[s[j]]] = j

        i_large(t, SA, s, bktl)
        i_small(t, SA, s, bkts)
        return SA
    return SAIS(m, n)
def LCP(s, n, sa):
    lcp = [-1]*(n+1)
    rank = [0]*(n+1)
    for i in xrange(n+1): rank[sa[i]] = i

    h = 0
    lcp[0] = 0
    for i in xrange(n):
        j = sa[rank[i] - 1]
        if h > 0: h -= 1
        while j+h < n and i+h < n and s[j+h]==s[i+h]:
            h += 1
        lcp[rank[i] - 1] = h
    return lcp

# SA-IS書き直し(20160604)
from collections import Counter
def SAIS(lst, num):
    l = len(lst)
    if l<2: return lst+[0]
    lst = lst + [0]
    l += 1
    res = [None] * l
    t = [1] * l
    for i in xrange(l-2, -1, -1):
        t[i] = 1 if lst[i]<lst[i+1] or (lst[i]==lst[i+1] and t[i+1]) else 0
    isLMS = [t[i-1]<t[i] for i in xrange(l)]
    LMS = [i for i in xrange(1, l) if t[i-1]<t[i]]
    LMSn = len(LMS)

    cbase = Counter(lst)
    count = cbase.copy()
    tmp = 0
    cstart = [0]*(num+1); cend = [0]*(num+1)
    for key in xrange(num+1):
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
            for i in xrange(l):
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
    for key in xrange(num+1):
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


# 1-dimension Rolling Hash
class RollingHash:
    def __init__(self, s, base, MOD):
        self.s = s
        self.l = l = len(s)
        self.base = base
        self.MOD = MOD
        self.h = h = [0]*(l + 1)
        for i in xrange(l):
            h[i+1] = (h[i] * base + ord(s[i])) % MOD
    def get(self, l, r):
        MOD = self.MOD
        return ((self.h[r] - self.h[l]*pow(self.base, r-l, MOD) + MOD)) % MOD
