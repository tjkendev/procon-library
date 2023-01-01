// dependent libraries
#include<vector>
#include<queue>
using namespace std;


#define LV 19
#define N 100005
 
// 入力: n, g
int n;
vector<int> g[N];
 
// 出力: root, g0, parent, level
int root;
vector<int> g0[N];
int parent[N], level[N];
 
bool c_used[N];
int sz[N];
int count_dfs(int v, int p) {
  int c = 1;
  for(int w : g[v]) {
    if(w == p || c_used[w]) continue;
    c += count_dfs(w, v);
  }
  return sz[v] = c;
}
 
int search_centroid(int v, int p, int s) {
  if((s - sz[v])*2 > s) {
    return -1;
  }
  bool ok = true;
  for(int w : g[v]) {
    if(w == p || c_used[w]) continue;
 
    int x = search_centroid(w, v, s);
    if(x != -1) {
      return x;
    }
    if(sz[w]*2 > s) {
      ok = false;
      break;
    }
  }
  return ok ? v : -1;
}
 
void centroid() {
  queue<int> que;
 
  int s = count_dfs(0, -1);
  int x = search_centroid(0, -1, s);
  que.push(x);
  c_used[x] = true;
  root = x;
  parent[x] = -1;
  level[x] = 0;
 
  while(!que.empty()) {
    int v = que.front(); que.pop();
    for(int w : g[v]) {
      if(c_used[w]) {
        continue;
      }
 
      int s = count_dfs(w, -1);
      int x = search_centroid(w, -1, s);
      g0[v].push_back(x);
      parent[x] = v;
      level[x] = level[v] + 1;
 
      que.push(x);
      c_used[x] = true;
    }
  }
}


// 重心分解の計算例: 各重心からの距離を計算
// dist[lv][u]: levelがlvの時、頂点uが含まれる部分木の重心頂点と頂点uの距離
int dist[LV][N];
// used: 計算用
int used[N];
void solve() {
  centroid();
  for(int u=0; u<n; u++) {
    queue<int> que;
    int lv = level[u];
    que.push(u);
    dist[lv][u] = 0;
    used[u] = u+1;
 
    while(!que.empty()) {
      int v = que.front(); que.pop();
      int dv = dist[lv][v];
      for(int w : g[v]) {
        if(level[w] < lv || used[w] == u+1) {
          continue;
        }
        dist[lv][w] = dv + 1;
      }
    }
  }
}