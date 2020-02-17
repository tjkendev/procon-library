# サイコロ: 長さ6 のリストで表現する
# L0 = [A, B, C, D, E, F]
#
# このリストは以下の展開図のサイコロを表現する
#  A
# DBCE
#  F
# 立方体のサイコロを上から見た図
#  E
# DAC (裏にF)
#  B

D = [
    (1, 5, 2, 3, 0, 4), # 'U'
    (3, 1, 0, 5, 4, 2), # 'R'
    (4, 0, 2, 3, 5, 1), # 'D'
    (2, 1, 5, 0, 4, 3), # 'L'
]
p_dice = (0, 0, 0, 1, 1, 2, 2, 3)*3

# サイコロを回転
def rotate_dice(L, k):
    return [L[e] for e in D[k]]

# サイコロL0 を回転しながら24種を列挙
def enumerate_dice(L0):
    L = L0[:]
    for k in p_dice:
        yield L
        L[:] = (L[e] for e in D[k])
