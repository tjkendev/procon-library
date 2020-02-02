template<typename T>
class WAVLTree {
  struct Node {
    Node *left, *right, *prt;
    T key;
    int rank, size;

    Node(T x) {
      left = right = prt = nullptr;
      rank = 0;
      key = x;
      size = 1;
    }

    inline bool is_left(Node *node) const {
      return left == node;
    }

    inline void assign(Node *node) {
      this->key = node->key;
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
      return m;
    }

    inline Node* rotate_double_left() {
      Node *r = this->right, *p = this->prt,
           *m = r->left, *ml = m->left, *mr = m->right;
      if((m->prt = p)) {
        if(p->left == this) p->left = m;
        else p->right = m;
      }
      if((this->right = ml)) ml->prt = this;
      if((r->left = mr)) mr->prt = r;
      m->left = this; this->prt = m;
      m->right = r; r->prt = m;

      int sz = this->size;
      this->size += (ml ? ml->size : 0) - r->size;
      r->size += (mr ? mr->size : 0) - m->size;
      m->size = sz;

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
      Node *n_node = node->left ? node->left : node->right;
      if(node->prt) {
        if(x < prt->key) {
          prt->left = n_node;
        } else {
          prt->right = n_node;
        }
        if(n_node) n_node->prt = prt;
        node = n_node;
      } else {
        if(n_node) n_node->prt = nullptr;
        this->root = n_node;
        node = nullptr;
      }
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

    Node *cur = prt;
    while(cur) {
      --cur->size;
      cur = cur->prt;
    }

    if(!prt) return;

    if(!prt->left && !prt->right && prt->rank == 1) {
      // 2,2-leaf
      prt->rank = 0;
      if(rank_diff(prt->prt, prt) <= 2) {
        return;
      }
      node = prt; prt = node->prt;
    }

    while(rank_diff(prt, node) == 3) {
      Node *sib = (prt->left == node ? prt->right : prt->left);
      if(!sib) {
        if(rank_diff(prt, sib) != 2) {
          break;
        }
        --prt->rank;
      } else {
        if(rank_diff(prt, sib) == 2) {
          --prt->rank;
        } else if(rank_diff(sib, sib->left) == 2 && rank_diff(sib, sib->right) == 2) {
          --prt->rank;
          --sib->rank;
        } else break;
      }
      node = prt; prt = node->prt;
    }

    if(rank_diff(prt, node) == 3) {
      if(prt->is_left(node)) {
        Node *sib = prt->right, *s_right = sib->right;
        if(rank_diff(sib, s_right) == 1) {
          // rotate
          prt->rotate_left();
          ++sib->rank;
          if(!prt->left && !prt->right) {
            prt->rank -= 2;
          } else {
            --prt->rank;
          }
          if(!sib->prt) {
            this->root = sib;
          }
        } else {
          // double rotate
          Node *s_left = sib->left;
          prt->rotate_double_left();
          if(!s_left->prt) {
            this->root = s_left;
          }
          prt->rank -= 2;
          s_left->rank += 2;
          --sib->rank;
        }
      } else {
        Node *sib = prt->left, *s_left = sib->left;
        if(rank_diff(sib, s_left) == 1) {
          // rotate
          prt->rotate_right();
          ++sib->rank;
          if(!prt->left && !prt->right) {
            prt->rank -= 2;
          } else {
            --prt->rank;
          }
          if(!sib->prt) {
            this->root = sib;
          }
        } else {
          // double rotate
          Node *s_right = sib->right;
          prt->rotate_double_right();
          if(!s_right->prt) {
            this->root = s_right;
          }
          prt->rank -= 2;
          s_right->rank += 2;
          --sib->rank;
        }
      }
    }
  }

  inline static int rank_diff(Node *prt, Node *node) {
    if(!prt) return 0;
    return (node ? prt->rank - node->rank : prt->rank + 1);
  }

public:
  WAVLTree() {
    root = nullptr;
  }

  // find a node with key x
  inline bool find(T x) {
    if(!this->root) {
      return false;
    }

    Node *node = find_node(this->root, x);
    return (node->key == x);
  }

  // find the k-th element.
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

  // insert a node with key x
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
    while(node) {
      ++node->size;
      node = node->prt;
    }

    node = new_node;
    while(node->prt) {
      Node *prt = node->prt;
      if(rank_diff(prt, prt->left) + rank_diff(prt, prt->right) != 1) {
        break;
      }
      ++prt->rank;
      node = prt;
    }

    if(!node->prt || rank_diff(node->prt, node) != 0) {
      return true;
    }

    Node *prt = node->prt;
    if(prt->is_left(node)) {
      Node *right = node->right;
      if(!right || rank_diff(node, right) == 2) {
        // rotate
        --prt->rank;
        prt->rotate_right();
      } else {
        // double rotate
        ++right->rank;
        --prt->rank;
        --node->rank;
        node = prt->rotate_double_right();
      }
    } else {
      Node *left = node->left;
      if(!left || rank_diff(node, left) == 2) {
        // rotate
        --prt->rank;
        prt->rotate_left();
      } else {
        // double rotate
        ++left->rank;
        --prt->rank;
        --node->rank;
        node = prt->rotate_double_left();
      }
    }
    if(!node->prt) {
      this->root = node;
    }
    return true;
  }

  // delete a node with key x
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

  // return the size of a tree
  int size() {
    return (this->root ? this->root->size : 0);
  }
};
