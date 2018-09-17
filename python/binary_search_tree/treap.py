# Treap
import random
random.seed()
class Treap:
    def __init__(self):
        self.root = None
        self.left = self.right = None
        self.ref = {}

    @staticmethod
    def __make(x, prob):
        # <the value of a node>, <the probability of a node>, <# of childs>, <left node>, <right node>, <parent node>, <prev node>, <next node>
        return [x, prob, 0, None, None, None, None, None]

    def empty(self):
        return not self.root

    def find_node(self, x):
        cur = self.root
        parent = cur
        if x in self.ref:
            return self.ref[x]
        while cur:
            if x == cur[0]:
                return cur
            if x < cur[0]:
                parent = cur
                cur = cur[3]
            else:
                parent = cur
                cur = cur[4]
        if parent and parent[0] < x and parent[7]:
            parent = parent[7]
        return parent

    def find_min(self, f):
        cur = self.root
        if not cur[6] and not cur[7]:
            return cur[0]
        left = self.left
        while 1:
            nxt = cur[7]
            if not nxt:
                if not cur[3]:
                    break
                cur = cur[3]
                continue
            val = f(nxt[0]) - f(cur[0])
            if val <= 0:
                left = cur
                if not cur[4]:
                    break
                cur = cur[4]
            else:
                if not cur[3]:
                    break
                cur = cur[3]
        if left[7] and f(left[0]) > f(left[7][0]):
            left = left[7]
        return left[0]

    @staticmethod
    def prev(node):
        return node[6]

    @staticmethod
    def next(node):
        return node[7]

    def remove(self, x):
        cur = self.find_node(x)
        if cur[0] != x:
            return False
        if cur[6]:
            cur[6][7] = cur[7]
        if cur[7]:
            cur[7][6] = cur[6]
        if self.left is cur:
            self.left = cur[7]
        if self.right is cur:
            self.right = cur[6]
        parent = cur[5]
        t = 3 if parent and x < parent[0] else 4
        while 1:
            if cur[3]:
                if cur[4]:
                    if cur[3][1] < cur[4][1]:
                        node = self.left_rotate(cur)
                        p = 3
                    else:
                        node = self.right_rotate(cur)
                        p = 4
                else:
                    node = self.right_rotate(cur)
                    p = 4
            else:
                if cur[4]:
                    node = self.left_rotate(cur)
                    p = 3
                else:
                    break
            if parent:
                parent[t] = node
            else:
                self.root = node
            parent = node; t = p
        if parent:
            parent[t] = None
        else:
            self.root = self.left = self.right = None
        del self.ref[x]
        del cur
        return True

    def insert(self, x):
        if x in self.ref:
            return self.ref[x]
        prob = random.random()
        new_node = self.__make(x, prob)
        self.ref[x] = new_node
        if not self.root:
            self.root = self.left = self.right = new_node
            return
        cur = self.root
        prv = nxt = None
        while 1:
            if x < cur[0]:
                nxt = cur
                if not cur[3]:
                    cur[3] = new_node
                    new_node[5] = cur
                    break
                cur = cur[3]
            else:
                prv = cur
                if not cur[4]:
                    cur[4] = new_node
                    new_node[5] = cur
                    break
                cur = cur[4]
        new_node[6] = prv; new_node[7] = nxt
        if prv:
            prv[7] = new_node
        if nxt:
            nxt[6] = new_node
        if (not self.left) or (x, prob) < (self.left[0], self.left[1]):
            self.left = new_node
        if (not self.right) or (self.right[0], -self.right[1]) < (x, -prob):
            self.right = new_node
        while cur:
            if x < cur[0]:
                cur[3] = new_node
                if prob <= cur[1]: break
                cur = self.right_rotate(cur)[5]
            else:
                cur[4] = new_node
                if prob <= cur[1]: break
                cur = self.left_rotate(cur)[5]
        if not cur:
            self.root = new_node
        return new_node

    @staticmethod
    def right_rotate(node):
        # assert node[3]
        left_node = node[3]
        B = left_node[4]
        left_node[4] = node; left_node[5] = node[5]
        node[3] = B; node[5] = left_node
        if B: B[5] = node
        return left_node

    @staticmethod
    def left_rotate(node):
        # assert node[4]
        right_node = node[4]
        B = right_node[3]
        right_node[3] = node; right_node[5] = node[5]
        node[4] = B; node[5] = right_node
        if B: B[5] = node
        return right_node

    def debug(self):
        tmp = []
        def dfs(node, level):
            if node[3]:
                dfs(node[3], level+1)
            tmp.append(" "*level + "(%d, %f)" % (node[0], node[1]))
            if node[4]:
                dfs(node[4], level+1)
        tmp.append("---")
        dfs(self.root, 0)
        tmp.append("---")
        print(*tmp, sep='\n')
        left = []; right = []
        node = self.root
        while node:
            left.append(node[0])
            node = node[6]
        node = self.root
        while node:
            right.append(node[0])
            node = node[7]
        print(*left, sep='<-')
        print(*right, sep='->')
