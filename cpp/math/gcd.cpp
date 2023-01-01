using ll = long long;

// Euclidean Algorithm
ll gcd(ll m, ll n) {
  ll r = m % n;
  return r ? gcd(n, r) : n;
}

// Extended Euclidean Algorithm
// - extgcd(a, b, x, y) -> a*x + b*y = d を満たす
ll extgcd(ll a, ll b, ll &x, ll &y) {
  if(b) {
    ll d = extgcd(b, a%b, y, x);
    y -= (a/b)*x;
    return d;
  }
  x = 1; y = 0;
  return a;
}