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
 
  ll query(int l, int r) {
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