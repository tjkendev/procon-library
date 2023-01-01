# *** 入力
# N: 文字列の長さ
# S: 文字列
# *** 出力
# sa[i]: SuffixArray
S = ...
N = len(S)

import functools

*SC, = map(ord, S+"$")

*sa, = range(N)

L = N + 1
rh = [0]*(L + 1)
md = [1]*(L + 1)
MOD = 2147483647
base = 37; rev = pow(base, MOD-2, MOD)
for i in range(1, L + 1):
    md[i] = md[i-1] * rev % MOD
cA = ord('a')
for i in range(L):
    rh[i+1] = (rh[i] * base + (SC[i] - cA)) % MOD

# lcp(i, j): S[i:] と S[j:] の最長共通接頭語(LCP)の長さを求める
def lcp(i, j):
    left = 0; right = N+1 - max(i, j)
    v = (rh[i]-rh[j]) % MOD
    while left+1 < right:
        mid = (left + right) >> 1
        if (rh[i+mid]-rh[j+mid])*md[mid] % MOD == v:
            left = mid
        else:
            right = mid
    return left

def cmp(a, b):
    k = lcp(a, b)
    return SC[a+k] - SC[b+k]
sa.sort(key=functools.cmp_to_key(cmp))