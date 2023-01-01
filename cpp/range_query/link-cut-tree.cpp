#include<algorithm>
using namespace std;
using ll = long long;


#define N 100003

class LinkCutTree {
  int n;
  int prt[N], left[N], right[N], sz[N], rev[N];
  ll key[N], val[N];

  void update(int i, int l, int r) {
    sz[i] = 1 + sz[l] + sz[r];
    val[i] = key[i] + val[l] + val[r];
  }

  void node_swap(int i) {
    if(i) {
      swap(left[i], right[i]);
      rev[i] ^= 1;
    }
  }

  bool prop(int i) {
    if(rev[i]) {
      node_swap(left[i]); node_swap(right[i]);
      rev[i] = 0;
      return true;
    }
    return false;
  }

  void splay(int i) {
    int x = prt[i];
    prop(i);

    int li = left[i], ri = right[i];
    while(x && (left[x] == i || right[x] == i)) {
      int y = prt[x];
      if(!y || (left[y] != x && right[y] != x)) {
        if(prop(x)) {
          swap(li, ri);
          node_swap(li); node_swap(ri);
        }

        if(left[x] == i) {
          left[x] = ri;
          prt[ri] = x;
          update(x, ri, right[x]);
          ri = x;
        } else {
          right[x] = li;
          prt[li] = x;
          update(x, left[x], li);
          li = x;
        }
        x = y;
        break;
      }

      prop(y);
      if(prop(x)) {
        swap(li, ri);
        node_swap(li); node_swap(ri);
      }

      int z = prt[y];
      if(left[y] == x) {
        if(left[x] == i) {
          int v = left[y] = right[x];
          prt[v] = y;
          update(y, v, right[y]);

          left[x] = ri; right[x] = y;
          prt[ri] = x;
          update(x, ri, y);

          prt[y] = ri = x;
        } else {
          left[y] = ri;
          prt[ri] = y;
          update(y, ri, right[y]);

          right[x] = li;
          prt[li] = x;
          update(x, left[x], li);

          li = x; ri = y;
        }
      } else {
        if(right[x] == i) {
          int v = right[y] = left[x];
          prt[v] = y;
          update(y, left[y], v);

          left[x] = y; right[x] = li;
          prt[li] = x;
          update(x, y, li);

          prt[y] = li = x;
        } else {
          right[y] = li;
          prt[li] = y;
          update(y, left[y], li);

          left[x] = ri;
          prt[ri] = x;
          update(x, ri, right[x]);

          li = y; ri = x;
        }
      }
      x = z;
      if(left[x] == y) {
        left[z] = i;
        update(z, i, right[z]);
      } else if(right[z] == y) {
        right[z] = i;
        update(z, left[z], i);
      } else break;
    }

    update(i, li, ri);
    left[i] = li; right[i] = ri;
    prt[li] = prt[ri] = i;
    prt[i] = x;

    rev[i] = prt[0] = 0;
  }

public:
  LinkCutTree(int n) {
    for(int i=0; i<n+1; ++i) prt[i] = left[i] = right[i] = rev[i] = 0, sz[i] = 1;
    sz[0] = 0; left[0] = right[0] = -1;
  }

  int expose(int i) {
    int p = 0, cur = i;
    while(cur) {
      splay(cur);
      right[cur] = p;
      update(cur, left[cur], p);
      p = cur;
      cur = prt[cur];
    }
    splay(i);
    return i;
  }

  int cut(int i) {
    expose(i);
    int p = left[i];
    left[i] = prt[p] = 0;
    return p;
  }

  int link(int i, int p) {
    expose(i);
    expose(p);
    prt[i] = p;
    right[p] = i;
  }

  int evert(int i) {
    expose(i);
    node_swap(i);
    prop(i);
  }
};
