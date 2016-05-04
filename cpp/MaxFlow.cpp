// Dinicアルゴリズム
// コンストラクタでnとsinkとsourceを決める。
// add_edge(s, t, cap)で辺追加。
// max_flow()で最大流を求める。
// グラフの変形がある場合は
//  - inc_edge(s, t, delta)[容量増加]
//  - dec_edge(s, t, delta)[容量減少]
// で変形を行う。
// 変形後はmax_flow()を使って求める。
struct Edge {
  int to, cap, rev;
  Edge(int t, int c, int r) : to(t), cap(c), rev(r) {}
  Edge() {}
};

#define MAX_N 1005

class Dinic {
  vector<Edge> g[MAX_N];
  int level[MAX_N], iter[MAX_N];
  int dist[MAX_N];
  int flow, n;
  int st, en;
  map<P, int> edges;

  void bfs(int s) {
    rep(i, n) level[i] = -1, dist[i] = INF;
    queue<int> que;
    level[s] = 0;
    que.push(s);
    while(!que.empty()) {
      int v = que.front(); que.pop();
      rep(i, g[v].size()) {
        Edge &e = g[v][i];
        if(e.cap > 0 && level[e.to] < 0) {
          level[e.to] = level[v] + 1;
          dist[e.to] = mind(e.cap, dist[v]);
          que.push(e.to);
        }
      }
    }
  }

  int dfs(int v, int t, int f) {
    if(v == t) return f;
    for(int &i=iter[v]; i<g[v].size(); ++i) {
      Edge &e = g[v][i];
      if(e.cap > 0 && level[v] < level[e.to]) {
        int d = dfs(e.to, t, mind(f, e.cap));
        if(d > 0) {
          e.cap -= d;
          g[e.to][e.rev].cap += d;
          return d;
        }
      }
    }
    return 0;
  }

public:
  Dinic(int n, int s, int t) {
    flow = 0;
    st = s; en = t;
    this->n = n;
  }

  // 有効辺の追加
  void add_edge(int from, int to, int cap) {
    edges[P(from, to)] = g[from].size();
    g[from].push_back(Edge(to, cap, g[to].size()));
    edges[P(to, from)] = g[to].size();
    g[to].push_back(Edge(from, 0, g[from].size()-1));
  }

  // 無向辺の追加
  void add_multi_edge(int v1, int v2, int cap) {
    edges[P(v1, v2)] = g[v1].size();
    g[v1].push_back(Edge(v2, cap, g[v2].size()));
    edges[P(v2, v1)] = g[v2].size();
    g[v2].push_back(Edge(v1, cap, g[v1].size()-1));
  }

  // 最大流を求める
  int max_flow(int s = -1, int t = -1, int rest = -1) {
    if(s == -1) s = st;
    if(t == -1) t = en;
    int su = 0;
    while(rest) {
      bfs(s);
      if(level[t] < 0) break;
      rep(i, n) iter[i] = 0;
      int f;
      while(rest && (f = dfs(s, t, rest == -1 ? INF : rest)) > 0) {
        if(rest == -1) {
          flow += f;
        } else {
          rest -= f;
        }
        su += f;
      }
    }
    return rest == -1 ? flow : su;
  }

  // 容量増加
  void inc_edge(int s, int t, int c) {
    P key = P(s, t);
    if(edges.find(key) != edges.end()) {
      g[s][edges[key]].cap += c;
    } else {
      add_edge(s, t, c);
    }
  }

  // 容量減少
  void dec_edge(int s, int t, int c) {
    P key = P(s, t);
    if(edges.find(key) != edges.end()) {
      int cap = g[s][edges[key]].cap;
      if(c <= cap) {
        g[s][edges[key]].cap -= c;
      } else {
        int rest = c - cap;

        g[s][edges[key]].cap = 0;
        g[t][edges[P(t, s)]].cap -= rest;

        bfs(s);
        if(level[t] >= 0) {
          // s -> t の残余グラフがあれば流す
          int ff = max_flow(s, t, rest);
          rest -= ff;
        }

        if(rest) {
          // end -> t, s -> start の残余グラフを流して
          // 全体の流す量を減らす
          int f1 = max_flow(en, t, rest);
          int f2 = max_flow(s, st, rest);

          //assert(f1 == f2 && f1 == rest && f2 == rest);
          flow -= rest;
        }
      }
    }
  }

  void debug() {
    rep(i, n) {
      rep(j, n) {
        if(i == j) continue;
        if(edges.find(P(i, j)) != edges.end()) {
          Edge &e = g[i][edges[P(i, j)]];
          cout << i SP j SP e.cap << endl;
        }
      }
    }
  }
};
