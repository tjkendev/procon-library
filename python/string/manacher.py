# 偶数長含めた回文の長さを求める
# R[2*i] = L: S[i]を中心とする奇数長の最大回文
# R[2*i+1] = L: S[i:i+2]を中心とする偶数長の最大回文
# ダミー文字を挟むが、各 R[i] は実際の回文の文字列長と一致する
def manacher(S):
    C = []
    for a in S:
        C.append(a)
        C.append(0)
    C.pop()

    L = len(C)

    R = [0]*L

    i = j = 0
    while i < L:
        while j <= i < L-j and C[i-j] == C[i+j]:
            j += 1
        R[i] = j
        k = 1
        while j-R[i-k] > k <= i < L-k:
            R[i+k] = R[i-k]
            k += 1
        i += k; j -= k

    for i in range(L):
        if i & 1 == R[i] & 1:
            R[i] -= 1
    return R
