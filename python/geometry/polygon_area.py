def polygon_area(N, P):
    return abs(sum(P[i][0]*P[i-1][1] - P[i][1]*P[i-1][0] for i in range(N))) / 2.

print(polygon_area(3, [(0, 0), (3, 1), (2, 5)]))
# => "6.5"