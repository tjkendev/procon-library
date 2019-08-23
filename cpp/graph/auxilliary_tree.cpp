#include<vector>
#include<algorithm>
using namespace std;

#define N 100000
#define NL 18
 
int fs[N], ls[N];
int depth[N];
int st[NL][3*N], lg[3*N];
 
int cur;
vector<int> g[N];
vector<int> g0[N];
 
void ett_dfs(int v, int p, int d) {
  st[0][fs[v] = cur++] = v;
  depth[v] = d;
  for(int w : g[v]) {
    if(w == p) continue;
    ett_dfs(w, v, d+1);
    st[0][cur++] = v;
  }
  ls[v] = cur-1;
}
 
void construct() {
  cur = 0;
  // Euler tour technique
  ett_dfs(0, -1, 0);
  lg[0] = lg[1] = 0;
  for(int i=2; i<=cur; ++i) lg[i] = lg[i >> 1] + 1;
 
  // Sparse Table
  for(int i=0, b=1; i<lg[cur]; ++i, b<<=1) {
    for(int j=0; j<(cur - (b<<1) + 1); ++j) {
      st[i+1][j] = (depth[st[i][j]] <= depth[st[i][j+b]] ? st[i][j] : st[i][j+b]);
    }
  }
}
 
bool cmp_at(int x, int y) {
  return fs[x] < fs[y];
}
 
int stk[2*N];
int auxilliary_tree(int k, int vs[2*N]) {
  sort(vs, vs+k, cmp_at);
  int k0 = k;
  for(int i=0; i<k-1; ++i) {
    int x = fs[vs[i]], y = fs[vs[i+1]];
    int l = lg[y - x + 1];
    int w = depth[st[l][x]] <= depth[st[l][y - (1 << l) + 1]] ? st[l][x] : st[l][y - (1 << l) + 1];
    vs[k0++] = w;
  }
  k = k0;
  sort(vs, vs+k, cmp_at);
  int prv = -1;
  int cur = 0;
  for(int i=0; i<k; ++i) {
    int v = vs[i];
    if(prv == v) continue;
    while(cur > 0 && ls[stk[cur-1]] < fs[v]) --cur;
    if(cur > 0) {
      g0[stk[cur-1]].push_back(v);
    }
    g0[v].clear();
    stk[cur++] = v;
    prv = v;
  }
  return k0;
}