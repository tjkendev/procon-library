// gcd(greatest common divisor)
ll gcd(ll m, ll n) {
  ll r = m % n;
  return r ? gcd(n, r) : n;
}

// extgcd(a, b, x, y)
// -> a*x + b*y = d を満たす
ll extgcd(ll a, ll b, ll &x, ll &y) {
  if(b) {
    d = extgcd(b, a%b, y, x);
    y -= (a/b)*x;
    return d;
  }
  x = 1; y = 0;
  return a;
}