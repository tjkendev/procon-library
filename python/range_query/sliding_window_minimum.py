# N: 要素列の長さ
# A[i]: 列のi番目の要素
# L: 最小値を調べる長さ

from collections import deque
A = [...]
L = ...

ans = []
que = deque()
for i, a in enumerate(A):
    while que and a <= que[-1][1]:
        que.pop()
    que.append((i, a))
 
    ans.append(que[0][1])
 
    if que and que[0][0] <= i+1-L:
        que.popleft()
 
ans = ans[L-1:]