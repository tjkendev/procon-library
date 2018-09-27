# N: クエリ処理する列のサイズ

data = [0]*(N+1)
def add(k, x):
    while k <= N:
        data[k] += x
        k += k & -k
 
def get(k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s