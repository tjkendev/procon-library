from collections import deque
deq = deque()
def check(f1, f2, f3):
    return (f2[0] - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])
def f(f1, x):
    return f1[0]*x + f1[1]

# add f_i(x) = a*x + b
def add_line(a, b):
    f1 = (a, b)
    while len(deq) >= 2 and check(deq[-2], deq[-1], f1):
        deq.pop()
    deq.append(f1)

# min f_i(x)
def query(x):
    while len(deq) >= 2 and f(deq[0], x) >= f(deq[1], x):
        deq.popleft()
    return f(deq[0], x)
