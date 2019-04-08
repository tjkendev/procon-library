#include<algorithm>
using ll = long long;
using namespace std;

#define N 100007

class SegmentTreeBeats {
  const ll inf = 1e18;
  int n, n0;
  ll max_d[4*N], smax_d[4*N];
  ll sum[4*N], cnt[4*N];

  void push(int k) {
    if(max_d[k] < max_d[2*k+1]) {
      sum[2*k+1] -= (max_d[2*k+1] - max_d[k]) * cnt[2*k+1];
      max_d[2*k+1] = max_d[k];
    }
    if(max_d[k] < max_d[2*k+2]) {
      sum[2*k+2] -= (max_d[2*k+2] - max_d[k]) * cnt[2*k+2];
      max_d[2*k+2] = max_d[k];
    }
  }

  void update(int k) {
    sum[k] = sum[2*k+1] + sum[2*k+2];

    if(max_d[2*k+1] < max_d[2*k+2]) {
      max_d[k] = max_d[2*k+2];
      cnt[k] = cnt[2*k+2];
      smax_d[k] = max(max_d[2*k+1], smax_d[2*k+2]);
    } else if(max_d[2*k+1] > max_d[2*k+2]) {
      max_d[k] = max_d[2*k+1];
      cnt[k] = cnt[2*k+1];
      smax_d[k] = max(smax_d[2*k+1], max_d[2*k+2]);
    } else {
      max_d[k] = max_d[2*k+1];
      cnt[k] = cnt[2*k+1] + cnt[2*k+2];
      smax_d[k] = max(smax_d[2*k+1], smax_d[2*k+2]);
    }
  }

  void _modify(ll x, int a, int b, int k, int l, int r) {
    if(b <= l || r <= a || max_d[k] <= x) {
      return;
    }
    if(a <= l && r <= b && smax_d[k] < x) {
      sum[k] -= (max_d[k] - x) * cnt[k];
      max_d[k] = x;
      return;
    }
    push(k);

    _modify(x, a, b, 2*k+1, l, (l+r)>>1);
    _modify(x, a, b, 2*k+2, (l+r)>>1, r);

    update(k);
  }

  ll _query_max(int a, int b, int k, int l, int r) {
    if(b <= l || r <= a) {
      return -inf;
    }
    if(a <= l && r <= b) {
      return max_d[k];
    }

    push(k);
    ll lv = _query_max(a, b, 2*k+1, l, (l+r)>>1);
    ll rv = _query_max(a, b, 2*k+2, (l+r)>>1, r);
    return max(lv, rv);
  }

  ll _query_sum(int a, int b, int k, int l, int r) {
    if(b <= l || r <= a) {
      return 0;
    }
    if(a <= l && r <= b) {
      return sum[k];
    }

    push(k);
    ll lv = _query_sum(a, b, 2*k+1, l, (l+r)>>1);
    ll rv = _query_sum(a, b, 2*k+2, (l+r)>>1, r);
    return lv + rv;
  }

public:
  SegmentTreeBeats(int n, ll *a=nullptr) : n(n) {
    n0 = 1;
    while(n0 < n) n0 <<= 1;
    for(int i=0; i<2*n0; ++i) {
      max_d[n0-1+i] = smax_d[n0-1+i] = -inf;
      cnt[n0-1+i] = 0;
      sum[n0-1+i] = 0;
    }
    if(a != nullptr) {
      for(int i=0; i<n; ++i) {
        max_d[n0-1+i] = sum[n0-1+i] = a[i];
        smax_d[n0-1+i] = -inf;
        cnt[n0-1+i] = 1;
      }
    } else {
      for(int i=0; i<n; ++i) {
        max_d[n0-1+i] = sum[n0-1+i] = 0;
        smax_d[n0-1+i] = -inf;
        cnt[n0-1+i] = 1;
      }
    }
    for(int i=n0-2; i >= 0; --i) update(i);
  }

  // range chmin [a, b)
  void update_chmin(int a, int b, ll x) {
    _modify(x, a, b, 0, 0, n0);
  }

  // range maximum query [a, b)
  ll query_max(int a, int b) {
    return _query_max(a, b, 0, 0, n0);
  }

  // range sum query [a, b)
  ll query_sum(int a, int b) {
    return _query_sum(a, b, 0, 0, n0);
  }
};
