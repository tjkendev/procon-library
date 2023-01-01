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

# query(a, b): S[a:] と S[b:] の最長共通接頭語(LCP)の長さを求める
# S = (文字列)
# N = len(S)
S = ...
N = len(S)

SA = SuffixArray(S)
sa = SA.suffix()
lcp = SA.lcp()
N0 = 2**(N).bit_length()
data = [0]*(2*N0)
for i in range(N+1):
    data[i+N0-1] = lcp[i]
for i in range(N0-2, -1, -1):
    data[i] = min(data[2*i+1], data[2*i+2])
D = [0]*(N+1)
for i, s in enumerate(sa):
    D[s] = i
def query(a, b):
    L = D[a] + N0; R = D[b] + N0
    if L > R:
        L, R = R, L
    s = N+1
    while L < R:
        if R & 1:
            R -= 1
            s = min(s, data[R-1])
 
        if L & 1:
            s = min(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s