// 強連結成分分解(Strongly Connected Component)
// int scc(): 結果は割り当てられた番号の数
// v: 頂点(0..v-1)
// g: 各頂点の出る辺, rg: 各頂点の逆辺
// group: 結果(閉路に１つの番号が割り当てられる)
#define V 10003
int v;
vector<int> g[V];
vector<int> rg[V];
int group[V];

vector<int> ord;
bool used[V];
void dfs(int s) {
  used[s] = true;
  rep(i, g[s].size()) {
    int t = g[s][i];
    if(!used[t]) {
      dfs(t);
    }
  }
  ord.push_back(s);
}

void rdfs(int s, int col) {
  group[s] = col;
  used[s] = true;
  rep(i, rg[s].size()) {
    int t = rg[s][i];
    if(!used[t]) {
      rdfs(t, col);
    }
  }
}

int scc() {
  rep(i, v) used[i] = false;
  rep(i, v) {
    if(!used[i]) dfs(i);
  }
  rep(i, v) used[i] = false;
  assert(ord.size() == v);
  int cnt = 0;
  repr(i, v) {
    int s = ord[i];
    if(!used[s]) rdfs(s, cnt++);
  }
  return cnt;
}