#include<algorithm>
using namespace std;
using ll = long long;

/* SegmentTree (一様区間足しこみ + 区間最小値) */
#define N_MAX (1 << 18)

class SegmentTree {
  int n;
  ll dmin[N_MAX], dadd[N_MAX];

  void _set(int a, int b, ll x, int k, int l, int r) {
    if(r <= a || b <= l) {
      return;
    }

    if(a <= l && r <= b) {
      dadd[k] += x;
      return;
    }

    _set(a, b, x, 2*k+1, l, (l+r)/2);
    _set(a, b, x, 2*k+2, (l+r)/2, r);

    ll lv = _get_value(2*k+1);
    ll rv = _get_value(2*k+2);
    dmin[k] = min(lv, rv);
  }

  ll _get_value(int k) {
    if(dmin[k] == dINF) {
      return dadd[k];
    }
    return dmin[k] + dadd[k];
  }

  ll _get(int a, int b, int k, int l, int r) {
    if(r <= a || b <= l) {
      return dINF;
    }
    if(a <= l && r <= b) {
      return _get_value(k);
    }
    ll lv = _get(a, b, 2*k+1, l, (l+r)/2);
    ll rv = _get(a, b, 2*k+2, (l+r)/2, r);
    if(min(lv, rv) == dINF) {
      return dadd[k];
    }
    return min(lv, rv) + dadd[k];
  }
public:
  const static ll dINF = 1e15;

  SegmentTree(int _n) {
    n = 1;
    while(n < _n) n <<= 1;
    for(int i=0; i<n; ++i) dmin[i] = dINF;
    for(int i=0; i<n; ++i) dadd[i] = 0;
  }

  void set(int a, int b, ll x) {
    _set(a, b, x, 0, 0, n);
  }

  ll get(int a, int b) {
    return _get(a, b, 0, 0, n);
  }

};