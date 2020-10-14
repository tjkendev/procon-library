def matmul(N, A, B, C):
    *TB, = zip(*B) # transpose
    for i in range(N):
        Ai = A[i]
        C[i][:] = (sum(Aik * Bkj for Aik, Bkj in zip(Ai, TBj)) for TBj in TB)
    return C

N = 3
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[1, 0, 1], [2, 1, 0], [0, 0, 1]]
C = [[0]*N for i in range(N)]
matmul(N, A, B, C)
print(C)
# => "[[5, 2, 4], [14, 5, 10], [23, 8, 16]]"