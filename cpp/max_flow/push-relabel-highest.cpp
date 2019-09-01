#include<vector>
using namespace std;
using ll = long long;


#define N 2000

class PushRelabel {
  const ll inf = 1e18;
  int n;
  struct Edge {
    int to;
    ll cap;
    int rev;
  };
  vector<Edge> g[N];

  int qs[N];
  // height, distance label, excess flow
  int hs[N], ds[N];
  ll fs[N];
  // active node
  bool active[N];
  // bucket
  vector<int> bs[N];
  int cur;

public:
  PushRelabel() {}
  PushRelabel(int n) { init(n); }
  inline void init(int n) { this->n = n; }

  inline void add_edge(int fr, int to, ll cap) {
    g[fr].emplace_back(Edge{to, cap, (int) g[to].size()});
    g[to].emplace_back(Edge{fr, 0, (int) g[fr].size()-1});
  }

  // Global labeling
  inline int bfs(int t) {
    int a = 0, b = 1;
    for(int i=0; i<n; ++i) hs[i] = n, ds[i] = 0, bs[i].clear();
    qs[0] = t;
    hs[t] = 0; ds[0] = 1;
    cur = 0;
    int d = 0;
    while(a < b) {
      int v = qs[a++];
      d = hs[v];
      for(Edge &e : g[v]) {
        int w = e.to;
        if(hs[w] <= d + 1 || g[w][e.rev].cap == 0) continue;
        hs[w] = d + 1;
        if(active[w] && d+1 < n) {
          bs[d+1].push_back(w);
          cur = d+1;
        }
        if(d+1 < n) ++ds[d+1];
        qs[b++] = w;
      }
    }
    return d+1;
  }

  inline ll flow(int s, int t) {
    for(int i=0; i<n; ++i) fs[i] = 0, active[i] = false;

    fs[s] = inf;
    active[s] = true;

    // initialize hs, bs, ds
    int gap = bfs(t);
    bs[cur].push_back(s);

    int cnt = 0;
    while(1) {
      while(cur >= 0 && bs[cur].size() == 0) --cur;
      if(cur < 0) break;

      int v = bs[cur].back(); bs[cur].pop_back();
      if(v == t) continue;

      int hv = hs[v];
      // Gap-relabeling
      if(hv > gap) {
        if(hv < n) --ds[hv];
        hs[v] = n;
        continue;
      }


      // push
      ll rest = fs[v];
      for(Edge &e : g[v]) {
        int w = e.to;
        if(e.cap > 0 && hv > hs[w] && hs[w] < gap) {
          ll d = min(rest, e.cap);
          e.cap -= d;
          g[w][e.rev].cap += d;
          rest -= d;
          fs[w] += d;
          if(!active[w]) {
            int hw = hs[w];
            bs[hw].push_back(w);
            if(cur < hw) cur = hw;
            active[w] = true;
          }
          if(rest == 0) break;
        }
      }
      fs[v] = rest;

      if(rest == 0) {
        active[v] = false;
        continue;
      }

      // relabel
      int h0 = hs[v];
      hv = n;
      for(Edge &e : g[v]) {
        int w = e.to;
        if(e.cap > 0 && hv > hs[w] + 1 && hs[w] < gap) {
          hv = hs[w] + 1;
        }
      }
      if(h0 != hv) {
        --ds[h0];
        if(ds[h0] == 0 && h0 < gap) {
          gap = h0;
          hv = n;
        } else if(hv == gap) {
          ++gap;
        }
        if(hv < n) ++ds[hv];
      }

      hs[v] = hv;
      if(hv < n) {
        bs[hv].push_back(v);
        if(cur < hv) cur = hv;
      } else {
        active[v] = false;
      }

      if((++cnt) % n == 0) {
        gap = bfs(t);
      }
    }
    return fs[t];
  }
};
