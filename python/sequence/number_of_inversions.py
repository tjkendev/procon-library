N = int(input())
*A, = map(int, input().split())

# BIT
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

ans = 0
for i, a in enumerate(A):
    # 自分より小さい要素がいくつ存在するかを計算
    ans += (N-1-i) - get(a)
    add(a, 1)
print(ans)