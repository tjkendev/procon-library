#include<vector>
using namespace std;

// ap[i]: 頂点iが関節点であればtrue

#define N 200005

int n;
vector<int> g[N];
bool ap[N];
int ord[N], low[N], lb = 0;
void dfs(int v, int p) {
  ord[v] = low[v] = lb++;
  int c = 0;
  for(int w : g[v]) {
    if(w == p) continue;
    if(ord[w] == -1) {
      dfs(w, v);
      ++c;
      ap[v] |= (ord[v] <= low[w]);
      low[v] = min(low[v], low[w]);
    } else {
      low[v] = min(low[v], ord[w]);
    }
  }
  if(p == -1) {
    ap[v] = (c > 1);
  }
}

void articulation() {
  for(int i=0; i<n; ++i) {
    ap[i] = false;
  }
  for(int i=0; i<n; ++i) {
    ord[i] = low[i] = -1;
  }
  for(int i=0; i<n; ++i) {
    if(ord[i] != -1) continue;
    dfs(i, -1);
  }
}