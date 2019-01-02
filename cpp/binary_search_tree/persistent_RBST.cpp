#define N 5000007
#define THRESHOLD 4800000

struct Node {
  Node *left, *right;
  ll v, sum, lazy;
  int count;
};

Node gnodes[2][N];
Node *nodes = gnodes[0];
int cur = 0, gcur = 0;

int count(Node *nd) {
  return nd != nullptr ? nd->count : 0;
}

ll sum(Node *nd) {
  return nd != nullptr ? nd->sum : 0;
}

Node *make_node(ll x) {
  Node *nd = &nodes[cur++];
  nd->v = nd->sum = x; nd->count = 1;
  nd->left = nd->right = nullptr;
  nd->lazy = 0;
  return nd;
}

Node *make_node(Node *left, Node *right, ll v = 0, ll lazy = 0) {
  Node *nd = &nodes[cur++];
  nd->left = left; nd->right = right;
  nd->v = v; nd->lazy = lazy;
  int c = 1 + count(left) + count(right);
  nd->sum = v + lazy*c+ sum(left) + sum(right);
  nd->count = c;
  return nd;
}

Node* dfs(Node *nd) {
  Node *left = nullptr, *right = nullptr;
  if(nd->left) left = dfs(nd->left);
  if(nd->right) right = dfs(nd->right);
  Node *r = &(nodes[cur++] = *nd);
  r->left = left; r->right = right;
  return r;
}

Node *rebuild(Node *root) {
  if(cur <= THRESHOLD) {
    return root;
  }
  nodes = gnodes[gcur = (gcur + 1) % 2];
  cur = 0;
  return dfs(root);
}

Node *n_add(Node *nd, ll lazy) {
  if(!nd || lazy == 0) return nd;
  Node *cnd = &(nodes[cur++] = *nd);
  cnd->lazy += lazy;
  cnd->sum += lazy * nd->count;
  return cnd;
}

Node *merge(Node *a, Node *b) {
  if(!a || !b) return !a ? b : a;
  if( rand() % (count(a) + count(b)) < count(a) ) {
    Node *p = n_add(a->left, a->lazy);
    Node *q = merge(n_add(a->right, a->lazy), b);
    return make_node(p, q, a->v + a->lazy, 0);
  } else {
    Node *p = merge(a, n_add(b->left, b->lazy));
    Node *q = n_add(b->right, b->lazy);
    return make_node(p, q, b->v + b->lazy, 0);
  }
}

pair<Node*, Node*> split(Node *nd, int k) {
  if(k <= 0 || !nd) {
    return pair<Node*, Node*>(nullptr, nd);
  }
  if(count(nd) <= k) {
    return pair<Node*, Node*>(nd, nullptr);
  }
  if(k <= count(nd->left)) {
    pair<Node*, Node*> d = split(nd->left, k);
    Node *a = d.first, *b = d.second;
    Node *q = make_node(b, nd->right, nd->v, nd->lazy);
    return make_pair(n_add(a, nd->lazy), q);
  }
  pair<Node*, Node*> d = split(nd->right, k - count(nd->left) - 1);
  Node *a = d.first, *b = d.second;
  Node *p = make_node(nd->left, a, nd->v, nd->lazy);
  return make_pair(p, n_add(b, nd->lazy));
}
