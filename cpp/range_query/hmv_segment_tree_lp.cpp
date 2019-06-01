#include<algorithm>
using namespace std;
typedef long long ll;

#define N (1 << 19)

class SegmentTree {
  static const ll inf = 1e18;

  struct Tag {
    ll ha, hb, a, b;

    Tag() {}

    Tag(ll a, ll b) : a(a), b(b) { ha = a; hb = b; }

    ll calc(ll x) const { return max(x + a, b); }
    ll hcalc(ll x) const { return max(x + ha, hb); }

    void merge(Tag &t) {
      if(a != -inf && t.ha != -inf) ha = max(ha, a + t.ha);
      if(b != -inf && t.ha != -inf) hb = max(hb, b + t.ha);
      hb = max(hb, t.hb);

      a = (a != -inf && t.a != -inf ? a + t.a : -inf);
      b = (b != -inf && t.a != -inf ? max(b + t.a, t.b) : t.b);
    }

    void clear() { a = ha = 0; b = hb = -inf; }

    bool empty() const { return a == 0 && b == -inf; }
  };

  int n0;
  ll max_v[2*N], hmax_v[2*N];
  Tag lazy[2*N];

  void push(int k) {
    if(n0-1 <= k) return;

    if(!lazy[k].empty()) {
      hmax_v[2*k+1] = max(hmax_v[2*k+1], lazy[k].hcalc(max_v[2*k+1]));
      max_v[2*k+1] = lazy[k].calc(max_v[2*k+1]);
      lazy[2*k+1].merge(lazy[k]);

      hmax_v[2*k+2] = max(hmax_v[2*k+2], lazy[k].hcalc(max_v[2*k+2]));
      max_v[2*k+2] = lazy[k].calc(max_v[2*k+2]);
      lazy[2*k+2].merge(lazy[k]);

      lazy[k].clear();
    }
  }

  void update(int k) {
    max_v[k] = max(max_v[2*k+1], max_v[2*k+2]);
    hmax_v[k] = max(hmax_v[2*k+1], hmax_v[2*k+2]);
  }

  ll _query_max(int a, int b, int k, int l, int r) {
    if(b <= l || r <= a) {
      return -inf;
    }
    if(a <= l && r <= b) {
      return max_v[k];
    }
    push(k);
    ll lv = _query_max(a, b, 2*k+1, l, (l+r)/2);
    ll rv = _query_max(a, b, 2*k+2, (l+r)/2, r);
    return max(lv, rv);
  }

  void _add_val(ll x, int a, int b, int k, int l, int r) {
    if(b <= l || r <= a) {
      return;
    }
    if(a <= l && r <= b) {
      Tag t = Tag(x, -inf);
      hmax_v[k] = max(hmax_v[k], t.hcalc(max_v[k]));
      max_v[k] = t.calc(max_v[k]);
      lazy[k].merge(t);
      return;
    }

    push(k);
    _add_val(x, a, b, 2*k+1, l, (l+r)/2);
    _add_val(x, a, b, 2*k+2, (l+r)/2, r);
    update(k);
  }

  void _update_val(ll x, int a, int b, int k, int l, int r) {
    if(b <= l || r <= a) {
      return;
    }
    if(a <= l && r <= b) {
      Tag t = Tag(-inf, x);
      hmax_v[k] = max(hmax_v[k], t.hcalc(max_v[k]));
      max_v[k] = t.calc(max_v[k]);
      lazy[k].merge(t);
      return;
    }

    push(k);
    _update_val(x, a, b, 2*k+1, l, (l+r)/2);
    _update_val(x, a, b, 2*k+2, (l+r)/2, r);
    update(k);
  }

  void _update_max(ll x, int a, int b, int k, int l, int r) {
    if(b <= l || r <= a) {
      return;
    }
    if(a <= l && r <= b) {
      Tag t = Tag(0, x);
      hmax_v[k] = max(hmax_v[k], t.hcalc(max_v[k]));
      max_v[k] = t.calc(max_v[k]);
      lazy[k].merge(t);
      return;
    }

    push(k);
    _update_max(x, a, b, 2*k+1, l, (l+r)/2);
    _update_max(x, a, b, 2*k+2, (l+r)/2, r);
    update(k);
  }

  ll _query_hmax(int a, int b, int k, int l, int r) {
    if(b <= l || r <= a) {
      return -inf;
    }
    if(a <= l && r <= b) {
      return hmax_v[k];
    }
    push(k);
    ll lv = _query_hmax(a, b, 2*k+1, l, (l+r)/2);
    ll rv = _query_hmax(a, b, 2*k+2, (l+r)/2, r);
    return max(lv, rv);
  }

public:
  SegmentTree(int n, ll *a) {
    n0 = 1;
    while(n0 < n) n0 <<= 1;

    for(int i=0; i<2*n0-1; ++i) lazy[i].clear();

    for(int i=0; i<n; ++i) max_v[n0-1+i] = hmax_v[n0-1+i] = a[i];
    for(int i=n; i<n0; ++i) max_v[n0-1+i] = hmax_v[n0-1+i] = -inf;

    for(int i=n0-2; i>=0; --i) update(i);
  }

  // range add query
  void add_val(int a, int b, ll x) {
    _add_val(x, a, b, 0, 0, n0);
  }

  // range update query
  void update_val(int a, int b, ll x) {
    _update_val(x, a, b, 0, 0, n0);
  }

  // range maximize query
  void update_max(int a, int b, ll x) {
    _update_max(x, a, b, 0, 0, n0);
  }

  // range maximum query
  ll query_max(int a, int b) {
    return _query_max(a, b, 0, 0, n0);
  }

  // (historic maximal value) range maximum query
  ll query_hmax(int a, int b) {
    return _query_hmax(a, b, 0, 0, n0);
  }
};
