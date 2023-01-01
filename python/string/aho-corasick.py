# この実装のnodeの説明
#
# node[0] ~ node[25]:
#     'a' ~ 'z'が来た時の次のnode (failure関数の遷移先も含まれる)
# node[-3] (node[27]):
#     いずれかの文字の終端であるかを示す(1 = 終端である)
# node[-2] (node[28]):
#     このnodeが何文字目に位置するかを表す
# node[-1] (node[29]):
#     このnodeでfailureした時の遷移先

from collections import deque
base = ord('a')
root = [None]*30
root[-2] = 0; root[-3] = 0

# 文字列sの追加
def add(s):
    node = root
    for c in s:
        code = ord(c) - base
        child = node[code]
        if not child:
            node[code] = child = [None]*30
            child[-2] = node[-2] + 1
            child[-3] = 0
        node = child
    node[-3] = 1

# BFSでfailure関数のリンクを構築
def suffix():
    que = deque([root])
    while que:
        v = que.popleft()
        for i in range(26):
            if not v[i]:
                if v[-1]:
                    v[i] = v[-1][i]
                else:
                    v[i] = root[i] or root
                continue
            if v[-1]:
                v[i][-1] = v[-1][i]
            else:
                v[i][-1] = root
            que.append(v[i])
    root[-1] = root
