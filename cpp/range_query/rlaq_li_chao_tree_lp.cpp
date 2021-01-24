#include <algorithm>

using ll = long long;
using namespace std;

const static ll inf = 1e18L;
class LiChaoTree {

  struct Line {
    ll a, b;

    Line(ll a, ll b) : a(a), b(b) {}
    Line() : a(0), b(0) {}

    inline ll f(ll x) const {
      return a * x + b;
    }

    Line& operator+=(const Line &ln) {
      if (b >= inf || ln.b >= inf) {
        a = 0; b = inf;
      } else {
        a += ln.a;
        b += ln.b;
      }
      return *this;
    }

    bool operator==(const Line &ln) const {
      return a == ln.a && b == ln.b;
    }
  };

  const Line line_inf = Line{0, inf};
  const Line line_zero = Line{0, 0};

  struct Node {
    Node *left, *right;
    Line line, lazy;

    Node(Line line) : left(nullptr), right(nullptr), line(line) {}
  };

  Node *root;
  ll xl, xr;

  inline bool compare(Line &l0, Line &l1, ll x) const {
    return l0.f(x) <= l1.f(x);
  }

  inline void _push_line(Node *nd, ll l, ll r) {
    if (nd == nullptr || nd->line == line_inf) return;

    ll m = (l + r) / 2;
    nd->left = _add_line(nd->left, nd->line, l, m);
    nd->right = _add_line(nd->right, nd->line, m, r);
    nd->line = line_inf;
  }

  inline void _add_lazy(Node *nd, Line &line) {
    if (nd == nullptr) return;

    nd->line += line;
    nd->lazy += line;
  }

  inline void _push_lazy(Node *nd, ll l, ll r) {
    if (nd == nullptr || nd->lazy == line_zero) return;

    _add_lazy(nd->left, nd->lazy);
    _add_lazy(nd->right, nd->lazy);
    nd->lazy = line_zero;
  }

  Node* _add_line(Node *nd, Line line, ll l, ll r) {
    if (l == r) return nullptr;

    ll m = (l + r) / 2;
    if (nd == nullptr) return new Node(line);

    _push_lazy(nd, l, r);

    bool left = compare(line, nd->line, l);
    bool mid = compare(line, nd->line, m);
    bool right = compare(line, nd->line, r);
    if (mid) {
      swap(nd->line, line);
    }
    if(r-l > 1 && left != right) {
      if (left != mid) {
        nd->left = _add_line(nd->left, line, l, m);
      } else {
        nd->right = _add_line(nd->right, line, m, r);
      }
    }
    return nd;
  }

  Node* _add_val(ll a, ll b, Node *nd, Line &line, ll l, ll r) {
    if (r <= a || b <= l) {
      return nd;
    }

    if (a <= l && r <= b) {
      _add_lazy(nd, line);
      return nd;
    }

    _push_lazy(nd, l, r);
    _push_line(nd, l, r);

    if (nd == nullptr) {
      nd = new Node(line_inf);
    }

    ll m = (l + r) / 2;
    nd->left = _add_val(a, b, nd->left, line, l, m);
    nd->right = _add_val(a, b, nd->right, line, m, r);
    return nd;
  }

  Node* _add_segment_line(ll a, ll b, Node *nd, Line &line, ll l, ll r) {
    if (r <= a || b <= l) {
      return nd;
    }
    if (a <= l && r <= b) {
      return _add_line(nd, line, l, r);
    }

    _push_lazy(nd, l, r);

    if (nd == nullptr) {
      nd = new Node(line_inf);
    }

    ll m = (l + r) / 2;
    nd->left = _add_segment_line(a, b, nd->left, line, l, m);
    nd->right = _add_segment_line(a, b, nd->right, line, m, r);
    return nd;
  }

  ll _query_min(ll k, ll l, ll r) {
    Node *nd = root;
    ll s = inf;
    while (r - l > 0 && nd != nullptr) {
      ll m = (l + r) / 2;

      _push_lazy(nd, l, r);

      s = min(s, nd->line.f(k));
      if (k < m) {
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
  LiChaoTree(ll xl, ll xr) : xl(xl), xr(xr), root(nullptr) {}

  // a_i <- min(a_i, a*i + b) for i in [xl, xr)
  void add_line(ll a, ll b) {
    Line line = Line{a, b};
    root = _add_line(root, line, xl, xr);
  }

  // a_i <- min(a_i, a*i + b) for i in [l, r)
  void add_segment_line(ll a, ll b, ll l, ll r) {
    Line line = Line{a, b};
    root = _add_segment_line(l, r, root, line, xl, xr);
  }

  // a_i <- a_i + (a*i + b) for i in [l, r)
  void add_val(ll a, ll b, ll l, ll r) {
    Line line = Line{a, b};
    root = _add_val(l, r, root, line, xl, xr);
  }

  // a_i <- +∞ for i in [l, r)
  void reset_val(ll l, ll r) {
    Line line = line_inf;
    root = _add_val(l, r, root, line, xl, xr);
  }

  // get a_i
  ll query_min(ll x) {
    return _query_min(x, xl, xr);
  }
};