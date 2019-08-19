#include<string>
using namespace std;
using ll = long long;

#define L 1000004

class RollingHash {
  ll base, mod;
  ll ptable[L];
  ll h[L];
  int sz;
public:
  RollingHash(string s, ll base, ll mod) : base(base), mod(mod) {
    sz = s.length();
    h[0] = 0;
    for(int i=0; i<sz; ++i) {
      h[i+1] = (h[i] * base + s[i]) % mod;
    }
    ptable[0] = 1;
    for(int i=0; i<sz; ++i) {
      ptable[i+1] = (ptable[i] * base) % mod;
    }
  }

  ll get(int l, int r) {
    // assert(0 <= l && r <= sz && l <= r);
    return (h[r] + ((mod - h[l]) * ptable[r-l] % mod)) % mod;
  }
};
