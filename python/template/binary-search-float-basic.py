def sqrt(x):
    def check(y):
        return y*y < x
    EPS = 1e-9
    left = 0; right = max(x, 1)
    while right - left > EPS:
        mid = (left + right) / 2
        if check(mid):
            left = mid
        else:
            right = mid
    return left

print(sqrt(0.5))
# => "0.7071067802608013"
print(sqrt(5))
# => "2.236067976919003"
# print(sqrt(5**21)) => 停止しない


from decimal import Decimal
def sqrt_d(x):
    def check(y):
        return y*y < x
    EPS = 1e-9
    left = Decimal(0); right = Decimal(max(x, 1))
    while right - left > EPS:
        mid = (left + right) / 2
        if check(mid):
            left = mid
        else:
            right = mid
    return left
print(sqrt_d(5**21))
# => "21836601.34277138317515660994"