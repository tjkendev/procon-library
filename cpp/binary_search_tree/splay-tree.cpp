struct Node {
  Node *left, *right;
  ll key;
  int count;

  Node(ll key, int count)
    : key(key), count(count), left(nullptr), right(nullptr) {}
};

// splay a node nd
Node* splay(stack<Node*> &st, stack<bool> &dr, Node* nd) {
  Node *l = nd->left, *r = nd->right;
  int L = (l ? l->count : 0), R = (r ? r->count : 0);
  int c = st.size() >> 1;
  Node *x, *y; bool d, d1;
  while(c--) {
    x = st.top(); st.pop();
    y = st.top(); st.pop();
    d = dr.top(); dr.pop();
    d1 = dr.top(); dr.pop();

    if(d == d1) {
      // Zig-zig step
      int e = (y->count -= L + R + 2);
      if(d) {
        y->right = x->left; x->left = y;
        x->right = l; l = x;

        l->count = (L += e + 1);
      } else {
        y->left = x->right; x->right = y;
        x->left = r; r = x;

        r->count = (R += e + 1);
      }
    } else {
      // Zig-zag step
      if(d) {
        x->right = l; l = x;
        y->left = r; r = y;

        L = (l->count -= R + 1);
        R = (r->count -= L + 1);
      } else {
        x->left = r; r = x;
        y->right = l; l = y;

        R = (r->count -= L + 1);
        L = (l->count -= R + 1);
      }
    }
  }

  if(!st.empty()) {
    // Zig step
    Node *x = st.top(); bool d = dr.top();
    if(d) {
      x->right = l; l = x;
      L = (l->count -= R + 1);
    } else {
      x->left = r; r = x;
      R = (r->count -= L + 1);
    }
  }

  nd->left = l; nd->right = r;
  nd->count = L + R + 1;

  return nd;
}

// merge a tree l with a tree r
Node* t_merge(Node *l, Node *r) {
  if(!l || !r) {
    return l ? l : r;
  }

  if(!l->right) {
    l->count += r->count;
    l->right = r;
    return l;
  }

  stack<Node*> st;
  stack<bool> dr;
  Node *x = l;
  while(x->right) {
    st.push(x); dr.push(true);
    x = x->right;
  }

  l = splay(st, dr, x);
  l->count += r->count;
  l->right = r;
  return l;
}

// split a tree t into two trees of size k and |t|-k
typedef pair<Node*, Node*> NodeP;
NodeP t_split(Node *t, int k) {
  if(!t || !(0 < k && k < t->count)) {
    return NodeP(t, nullptr);
  }
  Node *x = t;
  stack<Node*> st;
  stack<bool> dr;
  while(x) {
    Node *l = x->left;
    int c = (l ? l->count : 0) + 1;

    if(c == k) break;

    st.push(x);
    if(c < k) {
      k -= c;
      x = x->right;
      dr.push(true);
    } else {
      x = x->left;
      dr.push(false);
    }
  }
  Node *l = splay(st, dr, x), *r = l->right;
  if(r) l->count -= r->count;
  l->right = nullptr;
  return NodeP(l, r);
}

// insert a node with key = val
Node* insert(Node* t, ll val) {
  Node *nd = new Node(val, 1);
  stack<Node*> st;
  stack<bool> dr;
  Node *x = t, *y = nullptr;
  bool d;
  while(x) {
    st.push(y = x);
    dr.push(d = (x->key <= val));
    x->count++;
    x = (!d ? x->left : x->right);
  }
  if(!y) {
    return nd;
  }
  (!d ? y->left : y->right) = nd;
  return splay(st, dr, nd);
}

// delete a node with key = val
Node* remove(Node *t, ll val) {
  stack<Node*> st;
  stack<bool> dr;
  Node *x = t; bool d;
  while(x && x->key != val) {
    st.push(x);
    dr.push(d = (x->key <= val));
    x = (!d ? x->left : x->right);
  }
  if(!x) return t;

  t = splay(st, dr, x);
  return t_merge(t->left, t->right);
}

// find a node with key = val
Node* find(Node *t, ll val) {
  stack<Node*> st;
  stack<bool> dr;
  Node *x = t; bool d;
  while(x && x->key != val) {
    st.push(x);
    dr.push(d = (x->key <= val));
    x = (!d ? x->left : x->right);
  }
  if(!x) return t;

  return splay(st, dr, x);
}

// for debug
int dfs(Node *v, int k) {
  if(!v) return 0;
  int r = 0;
  if(v->left) r += dfs(v->left, k+1);
  rep(i, k) cout << " "; cout << v->key << " " << v->count << endl;
  if(v->right) r += dfs(v->right, k+1);
  return r+1;
}
