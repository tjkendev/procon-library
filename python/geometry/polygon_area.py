n = int(input())
p = [list(map(int, input().split())) for i in range(n)]
print(abs(sum(p[i][0]*p[i-1][1] - p[i][1]*p[i-1][0] for i in range(n))) / 2.)