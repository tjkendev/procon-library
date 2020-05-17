# ==== 切り上げ

def round_up0(p, q):
    if q < 0:
        p = -p; q = -q
    return (p + q - 1) // q

# ceil(p/q) = -floor(-(p/q))
def round_up1(p, q):
    return - (-p // q)

# ==== 切り捨て

def round_down(p, q):
    return p // q

# ==== 四捨五入

# floor((p/q) + (1/2))
def round_half_up0(p, q):
    return (2*p + q) // (2*q)

def round_half_up1(p, q):
    if q < 0:
        q = -q; p = -p
    x = p // q
    # x+(1/2) <= (p/q) の場合は +1 する
    if (2*x + 1)*q <= 2*p:
        x += 1
    return x

# ==== 五捨五超入

# ceil((p/q) - (1/2))
def round_half_down0(p, q):
    return - ((q - 2*p) // (2*q))

def round_half_down1(p, q):
    if q < 0:
        q = -q; p = -p
    x = p // q
    # x+(1/2) < (p/q) の場合は +1 する
    if (2*x + 1)*q < 2*p:
        x += 1
    return x

print(round_up0(10, 3))
# => "4"
print(round_up0(-10, 3))
# => "-3"
print(round_down(10, 3))
# => "3"
print(round_down(-10, 3))
# => "-4"

print(round_half_up0(30, 4))
# => "8"
print(round_half_down0(30, 4))
# => "7"