# Gregorian Calendar Date -> Modified Julian Date
def convert1(y, m, d):
    if m <= 2:
        m += 12
        y -= 1
    mjd = int(365.25*y) + (y//400) - (y//100) + int(30.59*(m-2)) + d - 678912
    return mjd

# Modified Julian Date -> Gregorian Calendar Date
def convert2(mjd):
    n = mjd + 678881
    a = 4*n + 3 + 4*(3*(4*(n+1)//146097+1)//4)
    b = 5*((a % 1461)//4) + 2
    y, m, d = a//1461, b//153 + 3, (b % 153)//5 + 1
    if m >= 13:
        y += 1
        m -= 12
    return y, m, d