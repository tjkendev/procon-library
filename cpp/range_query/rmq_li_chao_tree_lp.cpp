#include<algorithm>

using ll = long long;
using namespace std;

const static ll inf = 1e18L;
class LiChaoTree {

  struct Line {
    ll a, b;

    Line(ll a, ll b) : a(a), b(b) {}
    Line() : a(0), b(0) {}

    inline ll f(ll x) const {
      return a*x + b;
    }

    Line& operator+=(ll c) {
      if(b >= inf || c >= inf) {
        a = 0; b = inf;
      } else {
        b += c;
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
    Line line;
    ll lazy;
    ll v_min;

    Node(Line line) : left(nullptr), right(nullptr), line(line), lazy(0), v_min(inf) {}
  };

  Node *root;
  ll xl, xr;

  inline bool compare(Line &l0, Line &l1, ll x) const {
    return l0.f(x) <= l1.f(x);
  }

  inline void _update_node(Node *nd, ll l, ll r) {
    nd->v_min = min(nd->line.f(l), nd->line.f(r-1));
    if(nd->left) nd->v_min = min(nd->v_min, nd->left->v_min);
    if(nd->right) nd->v_min = min(nd->v_min, nd->right->v_min);
  }

  inline void _push_line(Node *nd, ll l, ll r) {
    if(nd == nullptr || nd->line == line_inf) return;

    ll m = (l + r) / 2;
    nd->left = _add_line(nd->left, nd->line, l, m);
    nd->right = _add_line(nd->right, nd->line, m, r);
    nd->line = line_inf;
  }

  inline void _add_lazy(Node *nd, ll &c) {
    if(nd == nullptr) return;

    nd->line += c;
    nd->lazy = (nd->lazy + c >= inf ? inf : nd->lazy + c);
    nd->v_min = (nd->v_min + c >= inf ? inf : nd->v_min + c);
  }

  inline void _push_lazy(Node *nd, ll l, ll r) {
    if(nd == nullptr || nd->lazy == 0) return;

    _add_lazy(nd->left, nd->lazy);
    _add_lazy(nd->right, nd->lazy);
    nd->lazy = 0;
  }

  Node* _add_line(Node *nd, Line line, ll l, ll r) {
    if(l == r) return nullptr;

    ll m = (l + r) / 2;
    if(nd == nullptr) {
      nd = new Node(line);
    } else {
      _push_lazy(nd, l, r);

      bool left = compare(line, nd->line, l);
      bool mid = compare(line, nd->line, m);
      bool right = compare(line, nd->line, r);
      if(mid) {
        swap(nd->line, line);
      }
      if(r-l > 1 && left != right) {
        if(left != mid) {
          nd->left = _add_line(nd->left, line, l, m);
        } else {
          nd->right = _add_line(nd->right, line, m, r);
        }
      }
    }

    _update_node(nd, l, r);
    return nd;
  }

  Node* _add_val(ll a, ll b, Node *nd, ll c, ll l, ll r) {
    if(r <= a || b <= l) {
      return nd;
    }

    if(a <= l && r <= b) {
      _add_lazy(nd, c);
      return nd;
    }

    _push_lazy(nd, l, r);
    _push_line(nd, l, r);

    if(nd == nullptr) {
      nd = new Node(line_inf);
    }

    ll m = (l + r) / 2;
    nd->left = _add_val(a, b, nd->left, c, l, m);
    nd->right = _add_val(a, b, nd->right, c, m, r);

    _update_node(nd, l, r);

    return nd;
  }

  Node* _add_segment_line(ll a, ll b, Node *nd, Line &line, ll l, ll r) {
    if(r <= a || b <= l) {
      return nd;
    }
    if(a <= l && r <= b) {
      return _add_line(nd, line, l, r);
    }

    _push_lazy(nd, l, r);

    if(nd == nullptr) {
      nd = new Node(line_inf);
    }

    ll m = (l + r) / 2;
    nd->left = _add_segment_line(a, b, nd->left, line, l, m);
    nd->right = _add_segment_line(a, b, nd->right, line, m, r);

    _update_node(nd, l, r);

    return nd;
  }

  ll _query_min(ll a, ll b, Node *nd, ll l, ll r) {
    if(nd == nullptr || b <= l || r <= a) {
      return inf;
    }

    if(a <= l && r <= b) {
      return nd->v_min;
    }

    _push_lazy(nd, l, r);

    ll m = (l + r) / 2;
    ll lv = _query_min(a, b, nd->left, l, m);
    ll rv = _query_min(a, b, nd->right, m, r);

    _update_node(nd, l, r);

    return min(
      min(lv, rv),
      min(nd->line.f(max(l, a)), nd->line.f(min(r, b)-1))
    );
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

  // a_i <- a_i + c for i in [l, r)
  void add_val(ll c, ll l, ll r) {
    root = _add_val(l, r, root, c, xl, xr);
  }

  // a_i <- +∞ for i in [l, r)
  void reset_val(ll l, ll r) {
    root = _add_val(l, r, root, inf, xl, xr);
  }

  // get min_{i in [l, r)} a_i
  ll query_min(ll l, ll r) {
    return _query_min(l, r, root, xl, xr);
  }
};