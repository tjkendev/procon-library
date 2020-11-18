#include<vector>
#include<unordered_map>

using namespace std;

template<typename K, typename V>
class PairingHeap {
  struct Node {
    Node *left, *right, *parent;
    K key;
    V value;

    void init(K key, V value) {
      this->key = key; this->value = value;
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

  inline static Node* link(Node *nd_a, Node *nd_b) {
    if(nd_a->key > nd_b->key) {
      swap(nd_a, nd_b);
    }
    Node *left = nd_a->left;
    nd_a->left = nd_b; nd_b->parent = nd_a;
    nd_b->right = left;
    if(left != nullptr) {
      left->parent = nd_b;
    }
    return nd_a;
  }

  inline Node* delete_min(Node *target) {
    if(target->left == nullptr) {
      return nullptr;
    }
    Node *cur = target->left, *prv = nullptr;
    while(cur != nullptr) {
      Node *sib = cur->right;
      if(sib == nullptr) {
        cur->parent = prv;
        prv = cur;
        break;
      }
      cur->parent = cur->right = nullptr;

      Node *nxt = sib->right;
      sib->parent = sib->right = nullptr;

      Node *merged = link(cur, sib);
      merged->parent = prv;
      prv = merged; cur = nxt;
    }

    Node *merged_tree = prv;
    cur = prv->parent;
    prv->parent = nullptr;
    while(cur != nullptr) {
      Node *nxt = cur->parent;
      cur->parent = nullptr;
      merged_tree = link(cur, merged_tree);
      cur = nxt;
    }
    return merged_tree;
  }

public:
  struct Result {
    K key;
    V value;
  };

  PairingHeap(int max_sz) {
    this->max_sz = max_sz;
    nds = new Node[max_sz];
    free_nodes.reserve(max_sz);
    init();
  }

  ~PairingHeap() {
    delete[] nds;
  }

  void clear() {
    init();
  }

  bool empty() const {
    return (root == nullptr);
  }

  // insert: O(1)
  void push(V value, K key) {
    Node *nd = new_node(key, value);
    if(root == nullptr) {
      root = nd;
    } else {
      root = link(root, nd);
    }
  }

  // delete-min: O(\log n) (amortized time)
  Result pop() {
    Node *target = root;
    Result result = {target->key, target->value};

    root = delete_min(target);

    remove_node(target);
    return result;
  }

  // decrease-key: O(\log n) (amortized time)
  void decrease_key(V value, K delta) {
    Node *target = nd_map[value];
    target->key -= delta;
    if(target->parent == nullptr) {
      return;
    }

    Node *parent = target->parent, *child = target->right;
    if(parent->left == target) {
      parent->left = child;
    } else {
      parent->right = child;
    }
    if(child != nullptr) {
      child->parent = parent;
    }

    target->right = target->parent = nullptr;
    root = link(root, target);
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
