#include<algorithm>
using namespace std;

template<typename T>
class AVLTree {
  struct Node {
    Node *left, *right, *prt;
    T key;
    int height, size;

    Node(T x) {
      left = right = prt = nullptr;
      height = 1;
      key = x;
      size = 1;
    }

    inline int factor() const {
      int lv = (this->left ? this->left->height : 0);
      int rv = (this->right ? this->right->height : 0);
      return (rv - lv);
    }

    inline int update_height() {
      return this->height = max(
        (this->left ? this->left->height : 0),
        (this->right ? this->right->height : 0)
      ) + 1;
    }

    inline bool is_left(Node *node) const {
      return left == node;
    }

    inline void assign(Node *node) {
      this->key = node->key;
    }

    inline Node* rotate_left() {
      Node *r = this->right, *m = r->left, *p = this->prt;
      if(r->prt = p) {
        if(p->left == this) p->left = r;
        else p->right = r;
      }
      if(this->right = m) m->prt = this;
      r->left = this; this->prt = r;

      int sz = this->size;
      this->size += (m ? m->size : 0) - r->size;
      r->size = sz;

      this->update_height();
      r->update_height();
      return r;
    }

    inline Node* rotate_right() {
      Node *l = this->left, *m = l->right, *p = this->prt;
      if(l->prt = p) {
        if(p->left == this) p->left = l;
        else p->right = l;
      }
      if(this->left = m) m->prt = this;
      l->right = this; this->prt = l;

      int sz = this->size;
      this->size += (m ? m->size : 0) - l->size;
      l->size = sz;

      this->update_height();
      l->update_height();
      return l;
    }

    inline Node* rotate_double_right() {
      Node *l = this->left, *p = this->prt,
           *m = l->right, *ml = m->left, *mr = m->right;
      if((m->prt = p)) {
        if(p->left == this) p->left = m;
        else p->right = m;
      }
      if((l->right = ml)) ml->prt = l;
      if((this->left = mr)) mr->prt = this;
      m->left = l; l->prt = m;
      m->right = this; this->prt = m;

      int sz = this->size;
      this->size += (mr ? mr->size : 0) - l->size;
      l->size += (ml ? ml->size : 0) - m->size;
      m->size = sz;

      this->update_height();
      l->update_height();
      m->update_height();

      return m;
    }

    inline Node* rotate_double_left() {
      Node *r = this->right, *p = this->prt,
           *m = r->left, *ml = m->left, *mr = m->right;
      if(m->prt = p) {
        if(p->left == this) p->left = m;
        else p->right = m;
      }
      if(this->right = ml) ml->prt = this;
      if(r->left = mr) mr->prt = r;
      m->left = this; this->prt = m;
      m->right = r; r->prt = m;

      int sz = this->size;
      this->size += (ml ? ml->size : 0) - r->size;
      r->size += (mr ? mr->size : 0) - m->size;
      m->size = sz;

      this->update_height();
      r->update_height();
      m->update_height();

      return m;
    }
  };

  Node *root;

  inline Node* find_node(Node *node, T x) {
    if(node == nullptr) return nullptr;
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

  inline void remove_node(Node *node) {
    T x = node->key;
    Node *prt = node->prt;

    if(!node->left || !node->right) {
      Node *n_node = (node->left ? node->left : node->right);
      if(prt) {
        if(x < prt->key) {
          prt->left = n_node;
        } else {
          prt->right = n_node;
        }
      }
      if((node = n_node)) node->prt = prt;
    } else {
      Node *c_node = find_node(node->right, x), *n_node = c_node->right;
      Node *c_prt = c_node->prt;
      if(node->right == c_node) {
        if((node->right = n_node)) n_node->prt = c_prt;
      } else {
        if((c_prt->left = n_node)) n_node->prt = c_prt;
      }
      node->assign(c_node);
      node = n_node; prt = c_prt;
    }

    while(prt) {
      --prt->size;
      prt->update_height();
      if(prt->is_left(node)) {
        if(prt->factor() == 2) {
          Node *sib = prt->right;
          if(sib->factor() < 0) {
            node = prt->rotate_double_left();
          } else {
            node = prt->rotate_left();
          }
        } else {
          if(prt->factor() == 1) break;
          node = prt;
        }
        prt = node->prt;
      } else {
        if(prt->factor() == -2) {
          Node *sib = prt->left;
          if(sib->factor() > 0) {
            node = prt->rotate_double_right();
          } else {
            node = prt->rotate_right();
          }
        } else {
          if(prt->factor() == -1) break;
          node = prt;
        }
        prt = node->prt;
      }
    }
    if(prt) {
      node = prt; prt = prt->prt;
      while(prt) {
        --prt->size;
        prt->update_height();
        node = prt; prt = node->prt;
      }
    }
    this->root = node;
  }

public:
  AVLTree() {
    root = nullptr;
  }

  inline bool find(T x) {
    if(!this->root) {
      return false;
    }

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
      this->root = new Node(x);
      return true;
    }

    Node *node = find_node(this->root, x);
    if(node->key == x) {
      return false;
    }

    Node *new_node = new Node(x);
    new_node->prt = node;
    if(x < node->key) {
      node->left = new_node;
    } else {
      node->right = new_node;
    }
    node = new_node;

    while(node->prt) {
      Node *prt = node->prt;
      ++prt->size;
      prt->update_height();
      if(prt->is_left(node)) {
        if(prt->factor() == -2) {
          if(node->factor() > 0) {
            node = prt->rotate_double_right();
          } else {
            node = prt->rotate_right();
          }
        } else {
          if(prt->factor() >= 0) break;
          node = prt;
        }
      } else {
        if(prt->factor() == 2) {
          if(node->factor() < 0) {
            node = prt->rotate_double_left();
          } else {
            node = prt->rotate_left();
          }
        } else {
          if(prt->factor() <= 0) break;
          node = prt;
        }
      }
    }
    if(node->prt) {
      node = node->prt;
      Node *prt = node->prt;
      while(prt) {
        ++prt->size;
        prt->update_height();
        node = prt; prt = node->prt;
      }
    }
    this->root = node;
    return true;
  }

  inline bool remove(T x) {
    if(!this->root) {
      return false;
    }

    Node *node = find_node(this->root, x);
    if(node->key != x) {
      return false;
    }

    remove_node(node);
    return true;
  }

  int size() {
    return (this->root ? this->root->size : 0);
  }
};
