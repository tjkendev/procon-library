# Convex Hull Trick: O((N + Q)logN) with Treap
class ConvexHullTrick:
    def __init__(self):
        self.A = Treap()
        self.B = {}

    def check(self, a1, a2, a3):
        B = self.B
        b1 = B[a1]; b2 = B[a2]; b3 = B[a3]
        return (a2-a1)*(b3-b2) >= (b2-b1)*(a3-a2)

    def add(self, a, b):
        B = self.B; A = self.A
        if a in B:
            if B[a] < b:
                return
            B[a] = b
            cur = A.find_node(a)
        else:
            B[a] = b
            node = A.find_node(a)
            if node and node[6]:
                a3 = node[6][0]; a1 = node[0]
                # a1 >= a >= a3
                if a1 >= a >= a3 and self.check(a1, a, a3):
                    del B[a]
                    return
                cur = A.insert(a)
            else:
                cur = A.insert(a)
        if cur and cur[6]:
            p = cur[6]
            while p and p[6] and p[7] and self.check(p[7][0], p[0], p[6][0]):
                v = p[0]; p = p[6]; A.remove(v)
                del B[v]
        if cur and cur[7]:
            p = cur[7]
            while p and p[6] and p[7] and self.check(p[7][0], p[0], p[6][0]):
                v = p[0]; p = p[7]; A.remove(v)
                del B[v]

    def empty(self):
        return not self.B

    def get(self, x):
        B = self.B
        calc = lambda a: a*x + B[a]
        if len(B) == 1:
            a, = B
            return calc(a)
        a = self.A.find_min(calc)
        return calc(a)

