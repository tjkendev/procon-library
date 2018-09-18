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