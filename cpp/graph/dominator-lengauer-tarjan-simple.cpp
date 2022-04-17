#include<vector>
using namespace std;

#define N 100003

int n;
vector<int> g[N];

vector<int> vs;
int order[N];
int prt[N];
int doms[N], semi[N];
int anc[N], label[N];
vector<int> rg[N], bucket[N];

inline void link(int v, int w) {
  anc[w] = v;
}

int compress(int v, int w) {
  if(w == anc[w]) {
    return w;
  }

  anc[v] = compress(w, anc[w]);
  if(semi[label[w]] < semi[label[v]]) {
    label[v] = label[w];
  }
  return anc[v];
}

inline int eval(int v) {
  if(v == anc[v]) {
    return v;
  }

  compress(v, anc[v]);
  return label[v];
}

void dfs(int v) {
  order[v] = vs.size();
  vs.push_back(v);
  for(int w : g[v]) {
    if(order[w] != -1) continue;
    prt[w] = v;
    dfs(w);
  }
}

void dominator(int s) {
  for(int i=0; i<n; ++i) order[i] = -1, prt[i] = -1;
  vs.reserve(n);

  dfs(s);

  for(int i=0; i<n; ++i) semi[i] = order[i], doms[i] = -1;
  for(int i=0; i<n; ++i) anc[i] = label[i] = i;

  for(int v=0; v<n; ++v) {
    for(int w : g[v]) {
      rg[w].push_back(v);
    }
  }

  for(int i=n-1; i>0; --i) {
    int w = vs[i];
    for(int v : bucket[w]) {
      int u = eval(v);
      doms[v] = (semi[u] < semi[v] ? u : w);
    }
    for(int v : rg[w]) {
      int u = eval(v);
      if(semi[u] < semi[w]) {
        semi[w] = semi[u];
      }
    }
    if(vs[semi[w]] != prt[w]) {
      bucket[vs[semi[w]]].push_back(w);
    } else {
      doms[w] = prt[w];
    }
    link(prt[w], w);
  }
  for(int v : bucket[s]) doms[v] = s;

  for(int i=1; i<n; ++i) {
    int w = vs[i];
    if(doms[w] != vs[semi[w]]) {
      doms[w] = doms[doms[w]];
    }
  }
  doms[s] = s;
}