import random

random.seed()
class RBST:
    def __init__(self):
        self.root = None

    # find a node with a key x
    def find(self, x):
        node = self.root
        while node:
            v = node[2]
            if v == x:
                return 1
            node = node[v < x]
        return 0

    # find the k-th key in a tree
    def at(self, k):
        node = self.root
        k += 1
        while 1:
            v = (node[0][3]+1 if node[0] else 1)
            if v == k:
                return node[2]
            if k < v:
                node = node[0]
            else:
                k -= v
                node = node[1]
        return -1

    # insert a node with a key x
    def insert(self, x):
        # before insert(x), the tree must not contain a key x
        rand = random.random
        new_node = [None, None, x, 1]
        if not self.root:
            self.root = new_node
            return
        node = self.root
        prv = None
        while node:
            if node[3] == int(rand() * (node[3]+1)):
                break
            node[3] += 1
            prv = node
            node = node[node[2] < x]
        if prv:
            prv[prv[2] < x] = new_node
        else:
            self.root = new_node

        left = right = new_node
        st = []
        while node:
            st.append(node)
            if node[2] < x:
                left[1] = left = node
                node = node[1]
            else:
                right[0] = right = node
                node = node[0]
        left[1] = right[0] = None
        new_node[0], new_node[1] = new_node[1], new_node[0]

        st.reverse()
        for node in st:
            l, r = node[:2]
            node[3] = (l[3] if l else 0) + (r[3] if r else 0) + 1
        l, r = new_node[:2]
        new_node[3] = (l[3] if l else 0) + (r[3] if r else 0) + 1

    # remove a node with key x
    def remove(self, x):
        # before remove(x), the tree must contain a key x
        rand = random.random
        node = self.root
        prt = None
        while node[2] != x:
            node[3] -= 1
            prt = node
            node = node[node[2] < x]

        cur = top = prt
        if prt:
            prv_d = (prt[1] == node)
        else:
            cur = top = [None]
            prv_d = 0
        left, right = node[:2]
        st = []; push = st.append
        while left and right:
            a = left[3]; b = right[3]
            if int(rand() * (a+b)) < a:
                push(left)
                cur[prv_d] = cur = left
                left = left[1]
                prv_d = 1
            else:
                push(right)
                cur[prv_d] = cur = right
                right = right[0]
                prv_d = 0
        rest = left or right
        cur[prv_d] = rest
        if not prt:
            self.root = top[0]

        st.reverse()
        for node in st:
            l, r = node[:2]
            node[3] = (l[3] if l else 0) + (r[3] if r else 0) + 1

    # pop the k-th key
    def pop(self, k):
        # when pop(x), the tree should contain the k-th element
        rand = random.random
        node = self.root
        prt = None
        k += 1
        while 1:
            l = node[0]
            v = (l[3]+1 if l else 1)
            if v == k:
                break
            prt = node
            node[3] -= 1
            if k < v:
                node = node[0]
            else:
                k -= v
                node = node[1]
        r_node = node

        cur = top = prt
        if prt:
            prv_d = (prt[1] == node)
        else:
            cur = top = [None]
            prv_d = 0
        left, right = node[:2]
        st = []; push = st.append
        while left and right:
            a = left[3]; b = right[3]
            if int(rand() * (a+b)) < a:
                push(left)
                cur[prv_d] = cur = left
                left = left[1]
                prv_d = 1
            else:
                push(right)
                cur[prv_d] = cur = right
                right = right[0]
                prv_d = 0
        rest = left or right
        cur[prv_d] = rest
        if not prt:
            self.root = top[0]

        st.reverse()
        for node in st:
            l, r = node[:2]
            node[3] = (l[3] if l else 0) + (r[3] if r else 0) + 1

        return r_node[2]
