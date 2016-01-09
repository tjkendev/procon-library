/* Segment木 */
#define SN 100003
class SegmentTree {
  ll data[SN];
  int n;

public:
  SegmentTree(int n_) {
    n = 1;
    while(n < n_) n *= 2;
    rep(i, 2*n) data[i] = 0;
  }

  void add(int k, ll a) {
    k += n - 1;
    data[k] += a;
    while(k > 0) {
      k = (k - 1) / 2;
      data[k] += a;
    }
  }

  ll _query(int a, int b, int k, int l, int r) {
    if(r <= a || b <= l) {
      return 0;
    }

    if(a <= l && r <= b) {
      return data[k];
    }

    ll vl = _query(a, b, 2*k+1, l, (l + r) / 2);
    ll vr = _query(a, b, 2*k+2, (l + r) / 2, r);
    return vl + vr;
  }

  ll query(int a, int b) {
    return _query(a, b, 0, 0, n);
  }
};


/* Binary Indexed Tree */
#define N 100003

class BIT {
  ll data[N];
  ll n;
public:
  BIT(int n) : n(n){}
  ll sum(int i) {
    ll s = 0;
    while(i > 0) {
      s += data[i];
      i -= i & -i;
    }
    return s;
  }
  void add(int i, ll x) {
    while(i <= n) {
      data[i] += x;
      i += i & -i;
    }
  }

};
