using ll = long long;

ll fast_pow(ll x, ll n, ll m) {
  ll r = 1;
  while(n > 0) {
    if(n & 1) {
      r = (r * x) % m;
    }
    x = (x * x) % m;
    n >>= 1;
  }
  return r;
}