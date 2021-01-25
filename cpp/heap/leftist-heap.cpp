#include<vector>
#include<unordered_map>

using namespace std;

template<typename K, typename V>
class LeftistHeap {
  struct Node {
    Node *left, *right, *parent;
    int npl;
    K key;
    V value;

    void init(K key, V value) {
      this->key = key; this->value = value;
      this->npl = 0;
      this->left = this->right = this->parent = nullptr;
    }
  };

  int max_sz;
  Node *nds;
  vector<Node*> free_nodes;

  Node *root;
  unordered_map<V, Node*> nd_map;

  void init() {
    free_nodes.clear();
    for(int i=0; i<max_sz; ++i) free_nodes.push_back(nds+i);
    root = nullptr;
  }

  Node* new_node(K key, V value) {
    // assert(free_nodes.size() > 0);
    Node *nd = free_nodes.back(); free_nodes.pop_back();
    nd->init(key, value);
    nd_map[value] = nd;
    return nd;
  }

  void remove_node(Node *node) {
    nd_map.erase(node->value);
    free_nodes.push_back(node);
  }

  static Node* merge(Node *nd_a, Node *nd_b) {
    if(nd_a == nullptr) return nd_b;
    if(nd_b == nullptr) return nd_a;
    if(nd_a->key > nd_b->key) {
      swap(nd_a, nd_b);
    }

    nd_a->right = merge(nd_a->right, nd_b);
    nd_a->right->parent = nd_a;
    if(nd_a->left == nullptr) {
      nd_a->left = nd_a->right; nd_a->right = nullptr;
      nd_a->npl = 0;
      return nd_a;
    }
    if(nd_a->left->npl < nd_a->right->npl) {
      swap(nd_a->left, nd_a->right);
    }
    nd_a->npl = nd_a->right->npl + 1;
    return nd_a;
  }

public:
  struct Result {
    K key;
    V value;
  };

  LeftistHeap(int max_sz) {
    this->max_sz = max_sz;
    nds = new Node[max_sz];
    free_nodes.reserve(max_sz);
    init();
  }

  ~LeftistHeap() {
    delete[] nds;
  }

  void clear() {
    init();
  }

  bool empty() const {
    return (root == nullptr);
  }

  void push(V value, K key) {
    Node *nd = new_node(key, value);
    if(root == nullptr) {
      root = nd;
    } else {
      root = merge(root, nd);
    }
  }

  Result pop() {
    Node *target = root;
    Result result = {target->key, target->value};

    Node *left = target->left, *right = target->right;
    root = merge(left, right);
    if(root != nullptr) {
      root->parent = nullptr;
    }

    remove_node(target);
    return result;
  }

  void decrease_key(V value, K delta) {
    Node *target = nd_map[value];
    target->key -= delta;
    if(target->parent == nullptr) {
      return;
    }

    Node *parent = target->parent;
    Node *child = merge(target->left, target->right);
    if(parent == nullptr) {
      root = child;
    } else if(parent->left == target) {
      parent->left = child;
    } else {
      parent->right = child;
    }
    if(child != nullptr) {
      child->parent = parent;
    }

    Node *cur = parent;
    while(cur != nullptr) {
      int lv = ((cur->left != nullptr) ? cur->left->npl : -1);
      int rv = ((cur->right != nullptr) ? cur->right->npl : -1);
      if(lv < rv) {
        swap(cur->left, cur->right);
      }
      int nv = min(lv, rv) + 1;
      if(nv == cur->npl) break;
      cur->npl = nv;

      cur = cur->parent;
    }

    target->left = target->right = target->parent = nullptr;
    root = merge(root, target);
  }

  void update(V value, K new_key) {
    if(nd_map.count(value) > 0) {
      Node *node = nd_map[value];
      K delta = node->key - new_key;
      // assert(delta >= 0);
      decrease_key(value, delta);
      return;
    }
    push(value, new_key);
  }
};