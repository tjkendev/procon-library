import cmath
pi = cmath.pi
exp = cmath.exp

# このFFTに与えるNは2**kにする
# 順変換・逆変換に与えるlistのサイズもNにする
N = 2**(n-1).bit_length()

def make_exp_t(N, base):
    exp_t = {0: 1}
    temp = N
    while temp:
        exp_t[temp] = exp(base / temp)
        temp >>= 1
    return exp_t

fft_exp_t = make_exp_t(N, -2j*pi)
ifft_exp_t = make_exp_t(N, 2j*pi)

def fft_dfs(f, s, N, st, exp_t):
    if N==2:
        a = f[s]; b = f[s+st]
        return [a+b, a-b]
    N2 = N//2; st2 = st*2
    F0 = fft_dfs(f, s   , N2, st2, exp_t)
    F1 = fft_dfs(f, s+st, N2, st2, exp_t)
    w = exp_t[N]; wk = 1.0
    for k in range(N2):
        U = F0[k]; V = wk * F1[k]
        F0[k] = U + V
        F1[k] = U - V
        wk *= w
    F0.extend(F1)
    return F0

def fft(f, N):
    if N==1:
        return f
    return fft_dfs(f, 0, N, 1, fft_exp_t)

def ifft(F, N):
    if N==1:
        return F
    f = fft_dfs(F, 0, N, 1, ifft_exp_t)
    for i in range(N):
        f[i] /= N
    return f

# F = fft(f, N)
# G = fft(g, N)
# FG = [a * b for a, b in zip(F, G)]
# fg = ifft(FG, N)