#include<vector>
#include<unordered_map>

using namespace std;

template<typename K, typename V>
class RankPairingHeap {
  struct Node {
    Node *left, *right, *parent;
    K key;
    V value;
    int rank;

    void init(K key, V value) const {
      this->key = key; this->value = value;
      this->left = this->right = this->parent = nullptr;
      this->rank = 0;
    }

    int left_rank() const {
      return left != nullptr ? left->rank : -1;
    }
    int right_rank() const {
      return right != nullptr ? right->rank : -1;
    }
  };

  Node *nds;
  int max_sz;
  vector<Node*> free_nodes, tmp;
  unordered_map<int, Node*> bucket;

  vector<Node*> roots;
  Node *min_root;
  unordered_map<V, Node*> nd_map;

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

  static Node* link(Node *nd_a, Node *nd_b) {
    if(nd_a->key > nd_b->key) {
      swap(nd_a, nd_b);
    }
    Node *left = nd_a->left;
    nd_a->left = nd_b; nd_b->parent = nd_a;
    nd_b->right = left;
    if(left != nullptr) {
      left->parent = nd_b;
    }
    nd_a->rank = nd_b->rank + 1;
    return nd_a;
  }

  void init() {
    min_root = nullptr;
    roots.clear(); free_nodes.clear();
    for(int i=0; i<max_sz; ++i) free_nodes.push_back(nds+i);
  }

public:
  struct Result {
    K key;
    V value;
  };

  RankPairingHeap(int max_sz) {
    this->max_sz = max_sz;
    nds = new Node[max_sz];
    free_nodes.reserve(max_sz);
    init();
  }

  ~RankPairingHeap() {
    delete[] nds;
  }

  void clear() {
    init();
  }

  bool empty() const {
    return (min_root == nullptr);
  }

  // insert: O(1)
  void push(V value, K key) {
    // assert(nd_map.count(value) == 0);
    Node *nd = new_node(key, value);
    if(min_root == nullptr) {
      min_root = nd;
    } else if(nd->key < min_root->key) {
      roots.push_back(min_root);
      min_root = nd;
    } else {
      roots.push_back(nd);
    }
  }

  // find-min: O(1)
  Result top() {
    // assert(!empty());      
    return Result{min_root->key, min_root->value};
  }

  // delete-min: O(\log N) (amortized time)
  Result pop() {
    // assert(!empty());

    Node *target = min_root;
    Result result = {target->key, target->value};

    tmp.clear();
    bucket.clear();
    for(Node *nd : roots) {
      int rank = nd->rank;
      if(bucket.count(rank)) {
        Node *root = bucket[rank]; bucket.erase(rank);
        Node *new_root = link(nd, root);
        tmp.push_back(new_root);
      } else {
        bucket[rank] = nd;
      }
    }

    Node *cur = min_root->left;
    while(cur != nullptr) {
      Node *nxt = cur->right;
      cur->right = cur->parent = nullptr;
      cur->rank = cur->left_rank() + 1;

      int rank = cur->rank;
      if(bucket.count(rank)) {
        Node *root = bucket[rank]; bucket.erase(rank);
        Node *new_root = link(cur, root);
        tmp.push_back(new_root);
      } else {
        bucket[rank] = cur;
      }
      cur = nxt;
    }
    for(pair<int, Node*> p : bucket) {
      tmp.push_back(p.second);
    }

    roots.clear();
    if(tmp.size() > 0) {
      int k = 0, min_key = tmp[0]->key;
      for(int i=1; i<tmp.size(); ++i) {
        if(tmp[i]->key < min_key) {
          min_key = tmp[i]->key;
          k = i;
        }
      }
      for(int i=0; i<tmp.size(); ++i) {
        if(i == k) continue;
        roots.push_back(tmp[i]);
      }
      min_root = tmp[k];
    } else {
      min_root = nullptr;
    }
    remove_node(target);
    return result;
  }

  // decrease-key: O(1) (amortized time)
  void decrease_key(V value, K delta) {
    Node *target = nd_map[value];
    target->key -= delta;
    if(target->parent == nullptr) {
      if(target->key < min_root->key) {
        swap(nd_map[target->value], nd_map[min_root->value]);
        swap(target->key, min_root->key);
        swap(target->value, min_root->value);
      }
      return;
    }

    Node *child = target->right;
    Node *u = target->parent;
    target->right = target->parent = nullptr;
    if(u->left == target) {
      u->left = child;
    } else {
      u->right = child;
    }
    if(child != nullptr) {
      child->parent = u;
    }

    while(true) {
      if(u->parent == nullptr) {
        u->rank = u->left_rank() + 1;
        break;
      }
      int lr = u->left_rank(), rr = u->right_rank();
      int k = (lr == rr ? lr + 1 : max(lr, rr));
      if(u->rank == k) break;

      u->rank = k;
      u = u->parent;
    }

    target->rank = target->left_rank() + 1;
    if(target->key < min_root->key) {
      roots.push_back(min_root);
      min_root = target;
    } else {
      roots.push_back(target);
    }
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