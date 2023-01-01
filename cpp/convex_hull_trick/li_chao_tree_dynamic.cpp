#include<algorithm>
using ll = long long;
using namespace std;

class LiChaoTree {
  struct Line {
    ll a, b;
    ll f(ll x) const { return a*x + b; }
    Line(ll a, ll b) : a(a), b(b) {}
  };
  struct Node {
    Node *left, *right;
    Line line;

    Node(Line line) : left(nullptr), right(nullptr), line(line) {}
  };
  const ll inf = 1e16L;
  const Line inf_line = Line{0, inf};

  Node* root;
  ll xl, xr;

  Node* _add_line(Node *nd, Line line, ll l, ll r) {
    if(l == r) return nullptr;

    ll m = (l + r) >> 1;
    if(nd == nullptr) return new Node(line);

    bool left = (line.f(l) <= nd->line.f(l));
    bool mid = (line.f(m) <= nd->line.f(m));
    bool right = (line.f(r) <= nd->line.f(r));
    if(left && right) {
      nd->line = line;
      return nd;
    }
    if(!left && !right) {
      return nd;
    }
    if(mid) {
      swap(nd->line, line);
    }
    if(left != mid) {
      nd->left = _add_line(nd->left, line, l, m);
    } else {
      nd->right = _add_line(nd->right, line, m, r);
    }
    return nd;
  }

  Node* _add_segment_line(ll a, ll b, Node *nd, Line line, ll l, ll r) {
    if(r <= a || b <= l) {
      return nd;
    }
    if(a <= l && r <= b) {
      return _add_line(nd, line, l, r);
    }

    if(nd == nullptr) {
      nd = new Node(inf_line);
    }

    ll m = (l + r) >> 1;
    nd->left = _add_segment_line(a, b, nd->left, line, l, m);
    nd->right = _add_segment_line(a, b, nd->right, line, m, r);
    return nd;
  }

  ll _query(ll k, ll l, ll r) {
    Node *nd = root;
    ll s = inf;
    while(r-l > 0 && nd != nullptr) {
      ll m = (l + r) >> 1;
      s = min(s, nd->line.f(k));
      if(k < m) {
        r = m;
        nd = nd->left;
      } else {
        l = m;
        nd = nd->right;
      }
    }
    return s;
  }

public:
  // [xl, xr)
  LiChaoTree(ll xl, ll xr) : xl(xl), xr(xr), root(nullptr) {}

  void add_line(ll a, ll b) {
    Line line = Line{a, b};
    root = _add_line(root, line, xl, xr);
  }

  void add_segment_line(ll a, ll b, ll l, ll r) {
    Line line = Line{a, b};
    root = _add_segment_line(l, r, root, line, xl, xr);
  }

  ll query(ll x) {
    return _query(x, xl, xr);
  }
};
