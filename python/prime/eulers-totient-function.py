# calculate φ(n)
def euler_phi(n):
  res = n
  for x in range(2, int(n**.5)+1):
    if n % x == 0:
      res = res // x * (x-1)
      while n % x == 0:
        n //= x
  return res

# calculate φ(x) for 1 <= x <= M
M = 10**6
*phi, = range(M+1)
for x in range(2, M+1):
  if phi[x] == x:
    for y in range(x, M+1, x):
      phi[y] = phi[y] // x * (x-1)