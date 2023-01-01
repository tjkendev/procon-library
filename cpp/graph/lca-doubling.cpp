#include<algorithm>
#include<queue>
#include<vector>
using namespace std;

#define N 100003
#define LEV 21

class LCADoubling {
  int n, lev;
  int kprv[LEV][N], de[N];

  inline void construct_kprv() {
    for(int k=0; k<lev; ++k) {
      for(int i=0; i<n; ++i) {
        if(kprv[k][i] == -1) continue;
        kprv[k+1][i] = kprv[k][kprv[k][i]];
      }
    }
  }

public:
  LCADoubling(int n) : n(n) {
    int n0 = 1;
    lev = 0;
    while(n0 < n) n0 <<= 1, ++lev;
  }
  void construct(int *prv, int *depth) {
    for(int i=0; i<n; ++i) kprv[0][i] = prv[i], de[i] = depth[i];
    construct_kprv();
  }

  void construct_from_graph(vector<int> g[N], int s) {
    bool used[N];
    queue<int> que;
    for(int i=0; i<n; ++i) used[i] = false;

    used[s] = true;
    kprv[0][s] = -1; de[s] = 0;
    que.push(s);
    while(!que.empty()) {
      int v = que.front(); que.pop();
      for(int i=0; i<g[v].size(); ++i) {
        int w = g[v][i];
        if(used[w]) continue;
        used[w] = true;
        kprv[0][w] = v; de[w] = de[v] + 1;
        que.push(w);
      }
    }
    construct_kprv();
  }

  int query(int u, int v) {
    int dd = de[v] - de[u];
    if(dd < 0) {
      swap(u, v);
      dd = -dd;
    }

    // de[u] <= de[v]
    for(int k=0; k<=lev; ++k) {
      if(dd & 1) {
        v = kprv[k][v];
      }
      dd >>= 1;
    }

    // de[u] == de[v]
    if(u == v) return u;

    for(int k=lev-1; k>=0; --k) {
      int pu = kprv[k][u], pv = kprv[k][v];
      if(pu != pv) u = pu, v = pv;
    }
    return kprv[0][u];
  }
};
