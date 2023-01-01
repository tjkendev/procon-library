#include<unordered_map>
#include<vector>
#include<algorithm>
using namespace std;
using ll = long long;


template<class T>
using comp_type = bool(const T &left, const T &right);
template<class T>
inline bool less_comp(const T &left, const T &right) { return left < right; }
template <class T>
inline bool greater_comp(const T &left, const T &right) { return left > right; }

template<class T, comp_type<ll> cmp = less_comp>
class FibonacciHeap {
  static const int deg_max = 25;

  struct Node {
    T key;
    ll dist;
    Node *prev = this, *next = this;

    bool mark = false;
    Node *parent = nullptr;
    Node *children = nullptr;
    int deg = 0;

    inline void add_child(Node* node) {
      ++deg;

      node->parent = this;
      if(deg == 1) {
        children = node;
        return;
      }
      Node *prev = children->prev;
      node->next = children;
      node->prev = prev;

      prev->next = node;
      children->prev = node;
    }

    inline void remove_child(Node *node) {
      --deg;

      node->parent = nullptr;
      if(deg == 0) {
        children = nullptr;
        return;
      }
      Node *prev = node->prev, *next = node->next;
      prev->next = next;
      next->prev = prev;
      if(node == children) {
        children = next;
      }
      node->prev = node->next = node;
    }

    inline Node* remove_all() {
      Node *c_nodes = children;
      children = nullptr;
      deg = 0;
      return c_nodes;
    }

    Node(T key, ll dist) : key(key), dist(dist) {}
    Node(T &&key, ll dist) : key(move(key)), dist(dist) {}
  };

  Node* top_node;
  Node* deglst[deg_max];
  unordered_map<T, Node*> node_map;
  int sz;

  inline bool add_root(Node *node) {
    if(top_node == nullptr) {
      top_node = node;
      node->prev = node->next = node;
      return false;
    }
    Node *prev = top_node->prev;
    node->prev = prev;
    node->next = top_node;

    prev->next = node;
    top_node->prev = node;
    return true;
  }

  inline void remove_root(Node *node) {
    Node *prev = node->prev, *next = node->next;
    next->prev = prev;
    prev->next = next;

    node->prev = node->next = node;
  }

  inline void insert_node(Node *node) {
    if(add_root(node)) {
      if(cmp(node->dist, top_node->dist)) {
        top_node = node;
      }
    }
    ++sz;
  }

  inline Node* pop_node() {
    Node* m_node = top_node;
    if(m_node == nullptr) {
      return nullptr;
    }

    Node *child = m_node->remove_all();
    if(child != nullptr) {
      Node *cur = child->next;
      child->parent = nullptr;
      child->prev = child->next = child;
      add_root(child);
      while(cur != child) {
        Node *next = cur->next;
        cur->parent = nullptr;
        cur->prev = cur->next = cur;
        add_root(cur);
        cur = next;
      }
    }

    if(sz == 1) {
      top_node = nullptr;
    } else {
      top_node = top_node->next;
      remove_root(m_node);
      consolidate();
    }
    --sz;
    return m_node;
  }

  inline void update_node(T &key, ll new_dist) {
    Node *node = node_map[key];
    node->dist = new_dist;

    Node *parent = node->parent;
    if(parent == nullptr || !cmp(new_dist, parent->dist)) {
      return;
    }

    while(1) {
      parent->remove_child(node);
      node->mark = false;
      add_root(node);

      if(parent->parent == nullptr) {
        break;
      }
      if(!parent->mark) {
        parent->mark = true;
        break;
      }
      node = parent; parent = parent->parent;
    }

    if(cmp(new_dist, top_node->dist)) {
      top_node = node;
    }
  }

  inline void consolidate() {
    Node *cur = top_node;

    for(int i=0; i<deg_max; ++i) deglst[i] = nullptr;
    Node *next = cur->next;
    do {
      cur = next; next = cur->next;
      Node *root = cur;
      remove_root(root);
      int d = root->deg;
      while(deglst[d] != nullptr) {
        Node* child = deglst[d];
        if(cmp(child->dist, root->dist)) {
          swap(root, child);
        }

        root->add_child(child);

        deglst[d++] = nullptr;
      }
      deglst[d] = root;
    } while(cur != top_node);

    top_node = nullptr;
    for(int i=0; i < deg_max; ++i) {
      Node *node = deglst[i];
      if(node == nullptr) continue;

      if(add_root(node)) {
        if(cmp(node->dist, top_node->dist)) {
          top_node = node;
        }
      }
    }
  }
public:
  FibonacciHeap() : sz(0), top_node(nullptr) {}

  int size() const { return sz; }
  bool empty() const { return sz == 0; }

  void push(T key, ll dist) {
    if(node_map.count(key)) {
      update_node(key, dist);
      return;
    }
    Node *node = new Node(key, dist);
    node_map[key] = node;
    insert_node(node);
  }

  void emplace(T &&key, ll dist) {
    if(node_map.count(key)) {
      update_node(key, dist);
      return;
    }
    Node *node = new Node(key, dist);
    node_map[key] = node;
    insert_node(node);
  }

  const pair<T, ll> top() const {
    return pair<T, ll>{top_node->key, top_node->dist};
  }

  void pop() {
    Node *node = pop_node();
    node_map.erase(node->key);
  }
};

const ll inf = 1e10;

#define N 100004

struct Edge {
  int to; ll cost;
};

int n;
ll dist[N];
vector<Edge> g[N];

void dijkstra(int s) {
  FibonacciHeap<int> que;
  que.push(s, 0);
  for(int i=0; i<n; ++i) dist[i] = inf;
  dist[s] = 0;

  while(!que.empty()) {
    pair<int, ll> p = que.top();
    ll co = p.second; int v = p.first;
    que.pop();
    //if(dist[v] < co) continue;
    for(auto &e : g[v]) {
      if(co + e.cost < dist[e.to]) {
        dist[e.to] = co + e.cost;
        que.push(e.to, dist[e.to]);
      }
    }
  }
}