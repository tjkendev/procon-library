# MOD上で 四則演算 + カッコ を処理する
#
# -- 文法規則 --
# S -> E
# E -> E '+' T | E '-' T | T
# T -> T '*' F | T '/' F | F
# F -> N | '(' E ')'
# N -> <数値>
def calc(S, MOD):
    L = len(S)
    S = S + "$"
    ok = 1
    cur = 0

    # E -> E '+' T | E '-' T | T
    def expr():
        nonlocal cur
        op = "+"
        res = 0
        while cur < L:
            val = term()
            if op == "+":
                res += val
            else: # '-'
                res -= val
            res %= MOD
            if S[cur] not in "+-":
                break
            op = S[cur]
            cur += 1 # '+' or '-'
        return res

    # T -> T '*' F | T '/' F | F
    def term():
        nonlocal cur, ok
        op = "*"
        res = 1
        while cur < L:
            val = factor()
            if op == "*":
                res *= val
            else: # '/'
                if val == 0:
                    ok = 0
                res *= pow(val, MOD-2, MOD)
            res %= MOD
            if S[cur] not in "*/":
                break
            op = S[cur]
            cur += 1 # '*' or '/'
        return res

    # F -> N | '(' E ')'
    def factor():
        nonlocal cur
        if S[cur] == '(':
            cur += 1 # '('
            val = expr()
            cur += 1 # ')'
            return val
        return number()

    # N -> <数値>
    def number():
        nonlocal cur
        val = 0
        while S[cur] in "0123456789":
            val = (10*val + int(S[cur])) % MOD
            cur += 1 # '0123456789'
        return val

    res = expr()
    return res if ok else -1

# example:
#   calc('100', 6) = 4
#   calc('10*3/7+(50+81/22)+11', 1153) = 915