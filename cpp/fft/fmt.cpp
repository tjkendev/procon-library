// 必要な依存関係
#include<algorithm>
#include<cassert>
using ll = long long;
using namespace std;

// x^n mod m
ll fast_pow(ll x, ll n, ll m) {
  ll r = 1;
  while(n) {
    if(n & 1) {
      r = (r * x) % m;
    }
    x = (x * x) % m;
    n >>= 1;
  }
  return r;
}
 
// Fast Modulo Transform
class FMT {
  int n;
  ll omega, omega_rev;
  ll p, n_rev;
  ll *tmp;
 
  // bit-reverse
  void bit_reverse(ll *d) {
    int i = 0;
    int ns = n >> 1, nss = n >> 2;
    for(int j = 0; j < ns; j += 2) {
      if(j < i) {
        swap(d[i], d[j]);
        swap(d[i+ns+1], d[j+ns+1]);
      }
      swap(d[i+1], d[j+ns]);
      int k = nss; i ^= k;
      while(k > i) {
        k >>= 1; i ^= k;
      }
    }
  }
 
  void fmt_calc(ll *a, ll base) {
    int n0 = n, m = 1;
    ll half = fast_pow(base, n/2, p);
    while(n0 > 1) {
      n0 >>= 1;
      ll w = fast_pow(base, n0, p), wk = 1;
      for(int j = 0; j < m; ++j) {
        for(int i = j; i < n; i += 2*m) {
          ll u = a[i], v = (a[i+m] * wk) % p;
          a[i] = (u + v) % p;
          a[i+m] = (u + (v*half) % p) % p;
        }
        wk = (wk * w) % p;
      }
      m <<= 1;
    }
  }
public:
  // p = a * n + 1 (n = 2^k)
  // -> omega^(p-1) ≡  1 (mod p)
  FMT(ll k, ll g, ll p) : p(p) {
    n = 1;
    while(k--) n <<= 1;
 
 
    assert((p-1) % n == 0);
    ll a = (p-1) / n;
    omega = fast_pow(g, a, p);
    omega_rev = fast_pow(omega, p-2, p);
    n_rev = fast_pow(n, p-2, p);
    tmp = new ll[n];
  }
 
  ~FMT() {
    delete tmp;
  }
 
  void fmt(ll *a, ll *result) {
    for(int i = 0; i < n; ++i) result[i] = a[i];
    bit_reverse(result);
    fmt_calc(result, omega);
  }
 
  void ifmt(ll *a, ll *result) {
    for(int i = 0; i < n; ++i) result[i] = (a[i] * n_rev) % p;
    bit_reverse(result);
    fmt_calc(result, omega_rev);
  }
 
  void convolute(ll *a, ll *b, ll *result) {
    fmt(a, tmp);
    fmt(b, result);
    for(int i = 0; i < n; ++i) tmp[i] = (result[i] * tmp[i]) % p;
    ifmt(tmp, result);
  }
 
  inline int size() const { return n; }
};

// example: FMT(17, 3, 1004535809)