#include<vector>
#include<set>
#include<cassert>
using namespace std;

// 強連結成分分解(Strongly Connected Component)
// n: 頂点(0..v-1)
// g: 各頂点の出る辺, rg: 各頂点の逆辺
// group: 結果(閉路に１つの番号が割り当てられる)
// label: 縮約後の頂点数
#define N 200003
struct SCC {
  int n;
  int group[N];
  int label;

  vector<int> *g, *rg;
  vector<int> ord;

  set<int> g0[N];
  vector<int> gp[N];
  int deg[N];

  bool used[N];
  void dfs(int v) {
    used[v] = true;
    for(int w : g[v]) {
      if(!used[w]) dfs(w);
    }
    ord.push_back(v);
  }

  void rdfs(int v, int col) {
    group[v] = col;
    used[v] = true;
    for(int w : rg[v]) {
      if(!used[w]) rdfs(w, col);
    }
  }

  // construct scc
  inline void init(int n, vector<int> *g, vector<int> *rg) {
    this->n = n; this->g = g; this->rg = rg;

    for(int i=0; i<n; ++i) used[i] = false;
    ord.reserve(n);
    for(int i=0; i<n; ++i) {
      if(!used[i]) dfs(i);
    }
    assert(ord.size() == n);

    for(int i=0; i<n; ++i) used[i] = false;
    int cnt = 0;
    for(int i=n-1; i>=0; --i) {
      int v = ord[i];
      if(!used[v]) rdfs(v, cnt++);
    }
    label = cnt;
  }

  inline void construct() {
    for(int i=0; i<n; ++i) deg[i] = 0;
    for(int v=0; v<n; ++v) {
      int s = group[v];
      for(auto w : g[v]) {
        int t = group[w];
        if(s == t || g0[s].count(t)) {
          continue;
        }

        g0[s].insert(t);
        ++deg[t];
      }

      gp[s].push_back(v);
    }
  }
};