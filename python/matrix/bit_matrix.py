# ビット行列演算
class BitMatrix:
    __slots__ = ['n', 'mat', 'mask', 'u', 'v']
    def __init__(self, n):
        self.n = n
        self.mat = 0
        self.u = u = 2**n - 1
        self.v = ((u+1)**n - 1) / u
    def copy(self, other):
        #assert self.n == other.n
        self.mat = other.mat
        return self

    def set(self, i, j, b):
        bit = 1 << (i*self.n + j)
        if b:
            self.mat |= bit
        else:
            self.mat &= ~bit
        return self
    def setZ(self):
        self.mat = 0
        return self
    def setI(self):
        n = self.n
        self.mat = (2**((n+1)*n) - 1) / (2**(n+1) - 1)
        return self
    def get(self, i, j):
        return (self.mat >> (i*self.n + j)) & 1
    def __add__(self, other):
        res = BitMatrix(self.n)
        res.mat = self.mat ^ other.mat
        return res
    def __iadd__(self, other):
        n = self.n
        self.mat ^= other.mat
        return self
    def __mul__(self, other):
        n = self.n; u = self.u; v = self.v
        res = BitMatrix(n)
        c = 0; a = self.mat; b = other.mat
        while a and b:
            c ^= ((a & v) * u) & ((b & u) * v)
            a >>= 1; b >>= n
        res.mat = c
        return res
    def __imul__(self, other):
        n = self.n; u = self.u; v = self.v
        c = 0; a = self.mat; b = other.mat
        while a and b:
            c ^= ((a & v) * u) & ((b & u) * v)
            a >>= 1; b >>= n
        self.mat = c
        return self
    def __pow__(self, k):
        res = BitMatrix(self.n).setI()
        A = BitMatrix(self.n).copy(self)
        while k:
            if k&1:
                res *= A
            A *= A
            k >>= 1
        return res
    def __ipow__(self, k):
        if k == 0:
            return self.setI()
        A = BitMatrix(self.n).copy(self)
        k -= 1
        while k:
            if k&1:
                self *= A
            A *= A
            k >>= 1
        return self