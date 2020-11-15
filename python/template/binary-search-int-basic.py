A = [1, 1, 1, 3, 3, 3, 3, 5, 5, 5]

# x 以下の最大の要素位置
def index_le(A, x):
    def check(y):
        return A[y] <= x
    left = -1; right = len(A)
    while left+1 < right:
        mid = (left + right) >> 1
        if check(mid):
            # e <= left は check(e) を満たす
            left = mid
        else:
            # right <= e は check(e) を満たさない
            right = mid
    return left
print([index_le(A, x) for x in range(0, 7)])
# => "[-1, 2, 2, 6, 6, 9, 9]"

# x 以上の最小の要素位置
def index_ge(A, x):
    def check(y):
        return x <= A[y]
    left = -1; right = len(A)
    while left+1 < right:
        mid = (left + right) >> 1
        if check(mid):
            # right <= e は check(e) を満たす
            right = mid
        else:
            # e <= left は check(e) を満たさない
            left = mid
    return right
print([index_ge(A, x) for x in range(0, 7)])
# => "[0, 0, 3, 3, 7, 7, 10]"
