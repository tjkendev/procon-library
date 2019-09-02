#include<algorithm>
using namespace std;
using ll = long long;

#define LV 20

class SegmentTree {
  const static ll inf = (1LL << 31) - 1;

  int n0, n;
  ll *data, *lazy;
  int ids[2*LV], cur = 0;

  void update_ids(int l, int r) {
    int l0 = (l + n0), r0 = (r + n0);
    int lb = (l0 & -l0) >> 1, rb = (r0 & -r0) >> 1;
    l0 >>= 1; r0 >>= 1;
    cur = 0;
    while(l0 > 0 && l0 < r0) {
      if(!rb) ids[cur++] = r0;
      if(!lb) ids[cur++] = l0;
      lb >>= 1; rb >>= 1;
      l0 >>= 1; r0 >>= 1;
    }
    while(l0 > 0) {
      ids[cur++] = l0;
      l0 >>= 1;
    }
  }

  void propagates() {
    for(int i=cur-1; i>=0; --i) {
      int k = ids[i];

      ll v = lazy[k-1];
      if(v == -1) continue;

      lazy[2*k-1] = data[2*k-1] = v;
      lazy[2*k] = data[2*k] = v;
      lazy[k-1] = -1;
    }
  }

public:

  SegmentTree(int n) : n(n) {
    n0 = 1;
    while(n0 < n) n0 <<= 1;
    data = new ll[2*n0];
    lazy = new ll[2*n0];
    for(int i=0; i<2*n0; ++i) data[i] = inf, lazy[i] = -1;
  }

  void update(int l, int r, ll x) {
    update_ids(l, r);
    propagates();

    int l0 = l + n0, r0 = r + n0;
    while(l0 < r0) {
      if(r0 & 1) {
        --r0;
        lazy[r0-1] = data[r0-1] = x;
      }
      if(l0 & 1) {
        lazy[l0-1] = data[l0-1] = x;
        ++l0;
      }
      l0 >>= 1; r0 >>= 1;
    }

    for(int i=0; i<cur; ++i) {
      int k = ids[i];
      data[k-1] = min(data[2*k-1], data[2*k]);
    }

  }

  ll query(int l, int r) {
    update_ids(l, r);
    propagates();

    int l0 = l + n0, r0 = r + n0;

    ll s = inf;
    while(l0 < r0) {
      if(r0 & 1) {
        --r0;
        s = min(s, data[r0-1]);
      }
      if(l0 & 1) {
        s = min(s, data[l0-1]);
        ++l0;
      }
      l0 >>= 1; r0 >>= 1;
    }
    return s;
  }
};
