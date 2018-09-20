# Randomized Binary Search Tree
from collections import namedtuple
Node = namedtuple('Node', ['l', 'r', 'v', 'sum', 'lazy', 'c'])
def new_node(l = None, r = None, v = 0, lazy = 0, Node=Node):
    sz = 1 + n_count(l) + n_count(r)
    return Node(l, r, v, v + lazy*sz + n_sum(l) + n_sum(r), lazy, sz)
 
def n_add(node, lazy):
    if not node:
        return None
    return node._replace(lazy=node.lazy+lazy, sum=node.sum + lazy * node.c)
 
def n_count(node):
    return node.c if node else 0
 
def n_sum(node):
    return node.sum if node else 0
 
import random
random.seed()
# aとbのどっちかを親にしてノードを生成
def merge(a, b, randint=random.randint):
    if not (a and b):
        return a if a else b
    # a=(Al, Ar), b = (Bl, Br)
    if randint(1-n_count(b), n_count(a)) > 0:
        # aを親にする
        # (Al, (Ar, b)) を生成して返す
        if not a.lazy:
            return new_node(a.l, merge(a.r, b), a.v, 0)
        p = n_add(a.l, a.lazy)
        q = merge(n_add(a.r, a.lazy), b)
        return new_node(p, q, a.v + a.lazy, 0)
    # bを親にする
    # ((a, Bl), Br) を生成して返す
    if not b.lazy:
        return new_node(merge(a, b.l), b.r, b.v, 0)
    p = merge(a, n_add(b.l, b.lazy))
    q = n_add(b.r, b.lazy)
    return new_node(p, q, b.v + b.lazy, 0)
 
# (A, B)を子に持つnodeを[0, k) [k, n)に分割
def split(node, k):
    if not k:
        # k == 0 --> [0, 0)は"None"
        return None, node
    if n_count(node) <= k:
        # |node|≧k --> [0, k) はnode全体
        return node, None
    if k <= n_count(node.l):
        # Aをa, bに分割
        # a = [0, k) b = [k, |A|)
        a, b = split(node.l, k)
        # (b, B)を持つノードqを生成
        q = new_node(b, node.r, node.v, node.lazy)
        # <a, q> を返す
        return (n_add(a, node.lazy), q) if node.lazy else (a, q)
    # Bをa, bに分割
    # a = [0, k-|A|-1), b = [k-|A|-1, |B|) になる
    a, b = split(node.r, k - n_count(node.l) - 1)
    # (A, a)を持つノードpを生成
    p = new_node(node.l, a, node.v, node.lazy)
    # <p, b> を返す
    return (p, n_add(b, node.lazy)) if node.lazy else (p, b)