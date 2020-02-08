#include<algorithm>
using namespace std;

template<typename T>
class AATree {
  struct Node {
    Node *left, *right, *prt;
    T key;
    int level, size;

    Node(T x) {
      left = right = prt = nullptr;
      level = 1;
      key = x;
      size = 1;
    }

    inline Node* rotate_left() {
      Node *r = this->right, *m = r->left, *p = this->prt;
      if((r->prt = p)) {
        if(p->left == this) p->left = r;
        else p->right = r;
      }
      if((this->right = m)) m->prt = this;
      r->left = this; this->prt = r;

      int sz = this->size;
      this->size += (m ? m->size : 0) - r->size;
      r->size = sz;

      return r;
    }

    inline Node* rotate_right() {
      Node *l = this->left, *m = l->right, *p = this->prt;
      if((l->prt = p)) {
        if(p->left == this) p->left = l;
        else p->right = l;
      }
      if((this->left = m)) m->prt = this;
      l->right = this; this->prt = l;

      int sz = this->size;
      this->size += (m ? m->size : 0) - l->size;
      l->size = sz;

      return l;
    }

    inline bool is_left(Node *node) const {
      return left == node;
    }

    inline void assign(Node *node) {
      this->key = node->key;
    }
  };

  Node *root;

  inline Node* find_node(Node *node, T x) {
    if(!node) return nullptr;

    while(node->key != x) {
      if(x < node->key) {
        if(!node->left) break;
        node = node->left;
      } else {
        if(!node->right) break;
        node = node->right;
      }
    }
    return node;
  }

  inline static Node* skew(Node *node) {
    if(!node) return nullptr;
    Node *left = node->left;
    if(left && node->level == left->level) {
      return node->rotate_right();
    }
    return node;
  }

  inline static Node* split(Node *node) {
    if(!node) return nullptr;
    Node *right = node->right;
    if(right && right->right && node->level == right->right->level) {
      Node* r = node->rotate_left();
      r->level += 1;
      return r;
    }
    return node;
  }

  inline static int get_level(Node *node) {
    return (node ? node->level : 0);
  }

public:
  AATree() {
    root = nullptr;
  }

  inline bool find(T x) {
    Node *node = find_node(this->root, x);
    return (node->key == x);
  }

  inline T at(int k) {
    if(!this->root) {
      return 0;
    }
    // assert(0 <= k < size);

    Node *node = this->root;
    ++k;
    while(1) {
      int l_size = (node->left ? node->left->size : 0) + 1;
      if(l_size == k) break;

      if(k < l_size) {
        node = node->left;
      } else {
        node = node->right;
        k -= l_size;
      }
    }
    return node->key;
  }

  inline bool insert(T x) {
    if(!this->root) {
      Node *new_node = new Node(x);
      this->root = new_node;
      return true;
    }

    Node *node = find_node(this->root, x);
    if(node->key == x) return false;

    Node *new_node = new Node(x);
    if(x < node->key) {
      node->left = new_node;
    } else {
      node->right = new_node;
    }
    new_node->prt = node;

    node = new_node;
    while(node) {
      node = split(skew(node));
      if(!node->prt) {
        this->root = node;
        break;
      }
      node = node->prt;
      ++node->size;
    }
    return true;
  }

  inline bool remove(T x) {
    if(!this->root) return false;

    Node *node = find_node(this->root, x);
    if(node->key != x) return false;

    if(node->left || node->right) {
      Node *c_node = find_node(!node->left ? node->right : node->left, x);
      node->assign(c_node);
      node = c_node;
    }

    Node *prt = node->prt;
    if(prt) {
      if(prt->is_left(node)) {
        prt->left = nullptr;
      } else {
        prt->right = nullptr;
      }
    } else {
      this->root = nullptr;
    }
    node = prt;

    while(node) {
      // decrease_key(node)
      int new_level = min(get_level(node->left), get_level(node->right)) + 1;
      if(new_level < node->level) {
        node->level = new_level;
        if(new_level < get_level(node->right)) {
          node->right->level = new_level;
        }
      }

      --node->size;
      node = skew(node);
      if(skew(node->right)) skew(node->right->right);

      node = split(node);
      split(node->right);

      if(!node->prt) {
        this->root = node;
        break;
      }
      node = node->prt;
    }

    return true;
  }

  int size() {
    return (this->root ? this->root->size : 0);
  }
};
