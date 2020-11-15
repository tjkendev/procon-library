import bisect

A = [1, 1, 1, 3, 3, 3, 3, 5, 5, 5]

# x 以下の最大の要素位置
def index_le(A, x):
    return bisect.bisect_right(A, x)-1
print([index_le(A, x) for x in range(0, 7)])
# => "[-1, 2, 2, 6, 6, 9, 9]"

# x 以上の最小の要素位置
def index_ge(A, x):
    return bisect.bisect_left(A, x)
print([index_ge(A, x) for x in range(0, 7)])
# => "[0, 0, 3, 3, 7, 7, 10]"