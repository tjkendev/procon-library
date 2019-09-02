using ll = long long;
#define N 100008

class BIT {
  int n;
  ll data[N];
 
public:
  BIT(int n) : n(n) {
    for(int i = 0; i < n+2; ++i) data[i] = 0;
  }
  void add(int k, ll x) {
    while(k <= n) {
      data[k] += x;
      k += k & -k;
    }
  }
 
  ll get(int k) {
    ll s = 0;
    while(k) {
      s += data[k];
      k -= k & -k;
    }
    return s;
  }
};