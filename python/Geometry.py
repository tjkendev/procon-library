
# 2点を通る2つの円を求める
# 半径1の実装だけど半径rに対しては
#  k = sqrt(r**2/(...) - 0.25)
# に変えればよい
from math import sqrt
def circle_center(x1, y1, x2, y2):
    xd = x2 - x1; yd = y2 - y1
    xc = (x1 + x2) / 2.0; yc = (y1 + y2) / 2.0
    k = sqrt(1.0/(xd**2 + yd**2) - 0.25)
    xd *= k; yd *= k
    return [[xc - yd, yc + xd], [xc + yd, yc - xd]]
