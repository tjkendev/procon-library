# Union-Find Tree
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.data = [0]*n
        for i in xrange(n):
            self.data[i] = i
    def root(self, x):
        if self.data[x] == x:
            return x
        self.data[x] = self.root(self.data[x])
        return self.data[x]
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx<ry:
            self.data[ry] = rx
        elif rx>ry:
            self.data[rx] = ry
    def match(self, x, y):
        return self.root(x)==self.root(y)
