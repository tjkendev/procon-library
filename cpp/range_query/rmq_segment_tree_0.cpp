#define N 100007
 
class SegmentTree {
  const static ll inf = (1LL << 31) - 1;
  int n, n0;
  ll data[4*N];
 
public:
  SegmentTree(int n) {
    n0 = 1;
    while(n0 < n) n0 <<= 1;
    rep(i, 2*n0) data[i] = inf;
  }
 
  void update(int k, ll x) {
    k += n0-1;
    data[k] = x;
    while(k > 0) {
      k = (k - 1) / 2;
      data[k] = min(data[2*k+1], data[2*k+2]);
    }
  }
 
  ll __query(int a, int b, int k, int l, int r) {
    if(a <= l && r <= b) {
      return data[k];
    }
    if(r <= a || b <= l) {
      return inf;
    }
    ll lv = __query(a, b, 2*k+1, l, (l+r)/2);
    ll rv = __query(a, b, 2*k+2, (l+r)/2, r);
    return min(lv, rv);
  }
 
  ll query(int a, int b) {
    return __query(a, b, 0, 0, n0);
  }
};