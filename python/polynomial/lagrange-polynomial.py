# ラグランジュ補完の多項式の係数計算
# N 個の点 (x_0, y_0), (x_1, y_1), ..., (x_{N-1}, y_{N-1}) について
# X = [x_0, x_1, ..., x_{N-1}]
# Y = [y_0, y_1, ..., y_{N-1}]
def build(X, Y):
    A = []
    for x in X:
        res = 1
        for xi in X:
            if x == xi:
                continue
            res *= x - xi
        A.append(Y[x] / res)
    return A
 
# 係数の値から f(k) の値を計算
# (全ての i について k != x_i とする)
def calc(X, A, k):
    # assert i not in X
    base = 1
    for xi in X:
        base *= k - xi
    return sum(base / (k - x) * a for x, a in zip(X, A))
