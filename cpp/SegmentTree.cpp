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
    dmin[k] = mind(lv, rv);
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
    if(mind(lv, rv) == dINF) {
      return dadd[k];
    }
    return mind(lv, rv) + dadd[k];
  }
public:
  const static ll dINF = 1e15;

  SegmentTree(int _n) {
    n = 1;
    while(n < _n) n <<= 1;
    rep(i, n) dmin[i] = dINF;
    rep(i, n) dadd[i] = 0;
  }

  void set(int a, int b, ll x) {
    _set(a, b, x, 0, 0, n);
  }

  ll get(int a, int b) {
    return _get(a, b, 0, 0, n);
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
