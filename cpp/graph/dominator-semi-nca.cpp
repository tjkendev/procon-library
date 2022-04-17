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
vector<int> rg[N];

inline void link(int v, int w) {
  anc[w] = v;
}

int compress(int v, int w) {
  if(w == anc[w]) {
    return w;
  }

  anc[v] = compress(w, anc[w]);
  if(label[w] < label[v]) {
    label[v] = label[w];
  }
  return anc[v];
}

inline int eval(int v) {
  if(v == anc[v]) {
    return label[v];
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

  for(int i=0; i<n; ++i) semi[i] = label[i] = order[i], doms[i] = -1;
  for(int i=0; i<n; ++i) anc[i] = i;

  for(int v=0; v<n; ++v) {
    for(int w : g[v]) {
      rg[w].push_back(v);
    }
  }

  for(int i=n-1; i>0; --i) {
    int w = vs[i];
    for(int v : rg[w]) {
      int s_min = eval(v);
      if(s_min < semi[w]) semi[w] = s_min;
    }
    label[w] = semi[w];
    link(prt[w], w);
  }

  doms[s] = s;
  for(int i=1; i<n; ++i) {
    int w = vs[i];
    int x = prt[w];
    while(semi[w] < order[x]) x = doms[x];
    doms[w] = x;
  }
}
