template<typename T>
class LeftLeaningRedBlackTree {
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

      r->color = this->color;
      this->color = RED;
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

      l->color = this->color;
      this->color = RED;
      return l;
    }

    inline void flip_color() {
      this->color ^= 1;
      this->left->color ^= 1;
      this->right->color ^= 1;
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

  inline Node* move_red_left(Node *node) {
    node->flip_color();

    Node *right = node->right;
    if(is_red(right->left)) {
      right->rotate_right();
      node = node->rotate_left();
      node->flip_color();
      if(!node->prt) this->root = node;
    }
    return node;
  }

  inline Node* move_red_right(Node *node) {
    node->flip_color();

    Node *left = node->left;
    if(is_red(left->left)) {
      node = node->rotate_right();
      node->flip_color();
      if(!node->prt) this->root = node;
    }
    return node;
  }

  inline Node* fixup(Node *node) {
    if(is_red(node->right) && is_black(node->left)) {
      node = node->rotate_left();
      if(!node->prt) this->root = node;
    }
    if(is_red(node->left) && is_red(node->left->left)) {
      node = node->rotate_right();
      if(!node->prt) this->root = node;
    }
    if(is_red(node->left) && is_red(node->right)) {
      node->flip_color();
    }
    return node;
  }

public:
  LeftLeaningRedBlackTree() {
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
      node = fixup(node)->prt;
    }
    this->root->color = BLACK;
    return true;
  }

  inline bool remove(T x) {
    Node *node = this->root;
    bool deleted = false;
    while(node) {
      if(x < node->key) {
        if(!node->left) break;

        if(is_black(node->left) && is_black(node->left->left)) {
          node = move_red_left(node);
        }
        node = node->left;
        continue;
      }

      if(is_red(node->left)) {
        node = node->rotate_right();
        if(!node->prt) this->root = node;
      }
      if(!node->right) {
        if(node->key == x) deleted = true;
        break;
      }
      if(is_black(node->right) && is_black(node->right->left)) {
        node = move_red_right(node);
      }
      if(node->key == x) {
        // delete_min(node->right);
        Node *c_node = node->right;
        while(c_node->left) {
          if(is_black(c_node->left) && is_black(c_node->left->left)) {
            c_node = move_red_left(c_node);
          }
          c_node = c_node->left;
        }
        node->assign(c_node);
        node = c_node;
        deleted = true;
        break;
      }
      node = node->right;
    }

    if(deleted) {
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
    }

    if(node) {
      while(node) {
        if(deleted) --node->size;
        node = fixup(node)->prt;
      }
      this->root->color = BLACK;
    }
    return true;
  }

  int size() {
    return (this->root ? this->root->size : 0);
  }
};
