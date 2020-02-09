template<typename T>
class RedBlackTree {
  enum NODE_COLOR { BLACK, RED };
  struct Node {
    Node *left, *right, *prt;
    T key;
    int color;
    int size;

    Node(T x) {
      left = right = prt = nullptr;
      color = RED;
      key = x;
      size = 1;
    }

    inline bool is_left(Node *node) const {
      return this->left == node;
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

    inline Node* get_sib(Node *node) {
      return (this->is_left(node) ? this->right : this->left);
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

  inline static bool is_red(Node *node) {
    return node && node->color == RED;
  }

  inline static bool is_black(Node *node) {
    return !node || node->color == BLACK;
  }

  inline void remove_node(Node *node) {
    Node *prt = node->prt;

    if(node->left && node->right) {
      Node *c_node = find_node(node->right, node->key);
      node->assign(c_node);
      node = c_node; prt = c_node->prt;
    }
    Node *dnode = node;

    Node *n_node = (node->left ? node->left : node->right);
    if(prt) {
      if(node->key < prt->key) {
        prt->left = n_node;
      } else {
        prt->right = n_node;
      }
    }
    if((node = n_node)) node->prt = prt;

    Node *cur = prt;
    while(cur) {
      --cur->size;
      cur = cur->prt;
    }

    if(is_red(dnode)) return;
    if(is_red(node)) {
      node->color = BLACK;
      if(!prt) this->root = node;
      return;
    }

    while(prt) {
      Node *sib = prt->get_sib(node);

      if(is_red(sib)) {
        if(prt->is_left(node)) {
          prt->rotate_left();
        } else {
          prt->rotate_right();
        }

        prt->color = RED;
        sib->color = BLACK;

        sib = prt->get_sib(node);
      }

      if(is_red(prt) || is_red(sib) || is_red(sib->left) || is_red(sib->right)) {
        if(is_red(prt) && is_black(sib) && is_black(sib->left) && is_black(sib->right)) {
          sib->color = RED;
          prt->color = BLACK;
          break;
        }

        if(is_black(sib)) {
          if(prt->is_left(node) && is_black(sib->right) && is_red(sib->left)) {
            Node *r = sib->rotate_right();
            r->color = RED;
            r->right->color = BLACK;
          } else if(!prt->is_left(node) && is_black(sib->left) && is_red(sib->right)) {
            Node *r = sib->rotate_left();
            r->color = RED;
            r->left->color = BLACK;
          }
          sib = prt->get_sib(node);
        }

        if(prt->is_left(node)) {
          prt->rotate_left();

          sib->color = prt->color;
          prt->color = sib->right->color = BLACK;
        } else {
          prt->rotate_right();

          sib->color = prt->color;
          prt->color = sib->left->color = BLACK;
        }
        break;
      }

      sib->color = RED;

      node = prt; prt = node->prt;
    }

    Node *n = (prt ? prt : node);
    if(n) {
      while(n->prt) n = n->prt;
    }
    this->root = n;
  }

public:
  RedBlackTree() {
    this->root = nullptr;
  }

  inline bool find(T x) {
    if(!this->root) return false;

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
      new_node->color = BLACK;
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

    while(node) {
      ++node->size;
      node = node->prt;
    }

    node = new_node;
    while(is_red(node->prt)) {
      Node *prt = node->prt;

      Node *gprt = prt->prt;
      Node *u = gprt->get_sib(prt);
      if(is_black(u)) {
        if(gprt->is_left(prt) && !prt->is_left(node)) {
          prt = prt->rotate_left();
          node = prt->left;
        } else if(!gprt->is_left(prt) && prt->is_left(node)) {
          prt = prt->rotate_right();
          node = prt->right;
        }

        if(prt->is_left(node)) {
          gprt->rotate_right();
        } else {
          gprt->rotate_left();
        }

        prt->color = BLACK;
        gprt->color = RED;

        break;
      }

      prt->color = u->color = BLACK;
      gprt->color = RED;

      node = gprt;
    }
    if(!node->prt) node->color = BLACK;

    while(node->prt) node = node->prt;
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
