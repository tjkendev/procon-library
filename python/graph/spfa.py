from collections import deque

INF = 10**18
# 返り値:
#  None (負閉路が存在した場合)
#  List[int] (それ以外)
def SPFA(N, G, s):
    dist = [INF] * N
    cont = [0] * N
    cnts = [0]* N

    dist[s] = 0
    cont[s] = 1
    cnts[s] += 1
    que = deque([s])
    while que:
        v = que.popleft()
        cont[v] = 0
        d = dist[v]
        for w, c in G[v]:
            if d + c < dist[w]:
                dist[w] = c + d
                if not cont[w]:
                    cnts[w] += 1
                    if N <= cnts[w]:
                        return None
                    if que and c + d < que[0]:
                        que.appendleft(w)
                    else:
                        que.append(w)
                    cont[w] = 1
    return dist