# Suffix Array (Manber & Myers) : O(n(logn)^2)
class SuffixArray:
    def __init__(self, s):
        self.s = s
        self.n = len(s)

    # Suffix Array
    def suffix(self):
        s = self.s; n = self.n
        rank = [0]*(n+1); sa = [0]*(n+1)
        tmp = [0]*(n+1)

        for i in range(n+1):
            sa[i] = i
            rank[i] = ord(s[i]) if i<n else -1

        k = 1
        cmp_key = lambda e: (rank[e], rank[e+k] if e+k<=n else -1)
        while k <= n:
            sa.sort(key=cmp_key)
            tmp[sa[0]] = 0
            for i in range(1, n+1):
                tmp[sa[i]] = tmp[sa[i-1]] + (cmp_key(sa[i-1])<cmp_key(sa[i]))
            for i in range(n+1):
                rank[i] = tmp[i]
            k *= 2

        self.sa = sa
        return sa

    # LCP Array
    def lcp(self):
        n = self.n; s = self.s; sa = self.sa
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
        self.lcp = lcp
        return lcp
