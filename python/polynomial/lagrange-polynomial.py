# ラグランジュ補完の多項式の係数計算
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
 
# 係数の値からf(x)の値を計算
def calc(X, A, x):
    base = 1
    for xi in X:
        base *= i - xi
    return sum(base / (i - x) * a for x, a in zip(X, A))