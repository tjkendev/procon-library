using ll = long long;

#define K 1003
#define MOD 1000000007
 
// (0-indexed)
// a[i] = a_i, c[i] = c_i
// a_{i+k} = c_i*a_i + c_{i+1}*a_{i+1} + ... + c_{i+k-1}*a_{i+k-1}
ll c[K], a[K];
 
// C(N, *) -> C(N+1, *)
void nxt(int k, ll c0[K], ll c1[K]) {
  c1[0] = (c0[k-1] * c[0]) % MOD;
  for(int i=0; i<k-1; ++i) {
    c1[i+1] = (c0[i] + c0[k-1]*c[i+1]) % MOD;
  }
}
 
// C(N, *) -> C(2N, *)
void dbl(int k, ll c0[K], ll c1[K]) {
  ll cs[K][K];
  for(int i=0; i<k; ++i) cs[0][i] = c0[i];
  for(int i=0; i<k-1; ++i) {
    nxt(k, cs[i], cs[i+1]);
  }
  for(int i=0; i<k; ++i) {
    c1[i] = 0;
    for(int j=0; j<k; ++j) {
      c1[i] += cs[0][j] * cs[j][i];
      c1[i] %= MOD;
    }
  }
}
 
// caluculate a_m
ll solve(int m, int k) {
  ll c0[K], c1[K];
  if(m == 0) {
    return a[0];
  }
  for(int i=0; i<k; ++i) c0[i] = 0;
  c0[1] = 1;
 
  int p = 31;
  while(((m >> --p) & 1) == 0);
  while(p-- > 0) {
    dbl(k, c0, c0);
    if((m >> p) & 1) {
      nxt(k, c0, c1);
      for(int j=0; j<k; ++j) c0[j] = c1[j];
    }
  }
 
  ll res = 0;
  for(int i=0; i<k; ++i) {
    res += c0[i]*a[i];
    res %= MOD;
  }
  return res;
}