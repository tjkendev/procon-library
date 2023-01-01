#include<deque>
using namespace std;
using ll = long long;

class ConvexHullTrick {
  struct F {
    ll a, b;
    F(ll a, ll b) : a(a), b(b) {}
  };

  deque<F> deq;

  bool check(F &f1, F &f2, F &f3) {
    return (f2.a - f1.a) * (f3.b - f2.b) >= (f2.b - f1.b) * (f3.a - f2.a);
  }

  ll f(F &f1, ll x) {
    return f1.a * x + f1.b;
  }

public:
  // a_{prev} >= a
  void add_line(ll a, ll b) {
    F f1 = F(a, b);
    while(deq.size() >= 2 && check(deq[deq.size()-2], deq[deq.size()-1], f1)) {
      deq.pop_back();
    }
    deq.push_back(f1);
  }

  // x_{prev} <= x
  ll query(ll x) {
    while(deq.size() >= 2 && f(deq[0], x) >= f(deq[1], x)) {
      deq.pop_front();
    }
    return f(deq[0], x);
  }
};