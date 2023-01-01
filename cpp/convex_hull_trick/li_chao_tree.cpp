#include<algorithm>
using namespace std;
using ll = long long;


#define N 300004

class LiChaoTree {
  static const ll inf = 1e9;
  static const ll infll = 1e18;

  int n;
  ll xs[4*N];
  ll p[4*N], q[4*N];
  bool u[4*N];

  void _add_line(ll a, ll b, int k, int l, int r) {
    while(r-l > 0) {
      int m = (l + r) >> 1;
      if(!u[k]) {
        p[k] = a; q[k] = b;
        u[k] = true;
        return;
      }

      ll lx = xs[l], mx = xs[m], rx = xs[r-1];
      ll pk = p[k], qk = q[k];
      bool left = (a*lx+b < pk*lx+qk);
      bool mid = (a*mx+b < pk*mx+qk);
      bool right = (a*rx+b < pk*rx+qk);
      if(left && right) {
        p[k] = a; q[k] = b;
        return;
      }
      if(!left && !right) {
        return;
      }
      if(mid) {
        swap(p[k], a);
        swap(q[k], b);
      }
      if(left != mid) {
        k = 2*k+1; r = m;
      } else {
        k = 2*k+2; l = m;
      }
    }
  }

  ll _query(int k, ll x) {
    k += n - 1;
    ll s = u[k] ? p[k]*x+q[k] : infll;
    while(k > 0) {
      k = (k - 1) / 2;
      if(u[k]) {
        ll r = p[k]*x+q[k];
        s = min(s, r);
      }
    }
    return s;
  }

public:
  LiChaoTree(int n0, ll ps[N]) {
    n = 1;
    while(n < n0) n <<= 1;

    for(int i=0; i<2*n; ++i) u[i] = false;
    for(int i=0; i<n0; ++i) xs[i] = ps[i];
    for(int i=n0; i<2*n-1; ++i) xs[i] = inf;
  }

  void add_line(ll a, ll b) {
    _add_line(a, b, 0, 0, n);
  }

  void add_segment_line(ll a, ll b, int l, int r) {
    ll l0 = l + n, r0 = r + n;
    ll s0 = l, t0 = r, sz = 1;
    while(l0 < r0) {
      if(r0 & 1) {
        --r0; t0 -= sz;
        _add_line(a, b, r0-1, t0, t0+sz);
      }
      if(l0 & 1) {
        _add_line(a, b, l0-1, s0, s0+sz);
        ++l0; s0 += sz;
      }
      l0 >>= 1; r0 >>= 1;
      sz <<= 1;
    }
  }

  ll query(int i) {
    return _query(i, xs[i]);
  }
};