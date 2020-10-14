from operator import itemgetter
# caluculate a logical matrix C s.t. AB = C
# - A, B and C are N×N logical matrices
def matmul(N, A, B, C):
    F = [itemgetter(j) for j in range(N)]
    for i in range(N):
        B0 = [Bk for Aik, Bk in zip(A[i], B) if Aik]
        C[i][:] = (sum(map(f, B0)) & 1 for f in F)
    return C

N = 3
A = [[1, 0, 1], [0, 1, 1], [1, 1, 0]]
B = [[1, 0, 0], [1, 1, 0], [0, 0, 1]]
C = [[0]*N for i in range(N)]
matmul(N, A, B, C)
print(C)
# => "[[1, 0, 1], [1, 1, 1], [0, 1, 0]]"