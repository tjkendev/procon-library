#include<vector>
#include<queue>
using namespace std;
using ll = long long;
using P = pair<int, int>;


#define MAX_N 107
class MinCostFlow {
  static const ll inf = 1e18;
  struct Edge {
    int to, cap, cost;
    size_t rev;
  };
 
  vector<Edge> g[MAX_N];
  int h[MAX_N];
  int prv_v[MAX_N], prv_e[MAX_N];
  ll dist[MAX_N];
  int n;
 
public:
  MinCostFlow(int n) : n(n) {}
 
  void add_edge(int fr, int to, int cap, int cost) {
    g[fr].emplace_back(Edge{to, cap, cost, g[to].size()});
    g[to].emplace_back(Edge{fr, 0, -cost, g[fr].size()-1});
  }
 
  ll flow(int s, int t, ll f) {
    ll res = 0;
    for(int i=0; i<n; ++i) h[i] = prv_v[i] = prv_e[i] = 0;
 
    while(f) {
      for(int i=0; i<n; ++i) dist[i] = inf;
      dist[s] = 0;
 
      priority_queue<P, vector<P>, greater<P> > que;
      que.push(P(0, s));
      while(!que.empty()) {
        P p = que.top(); que.pop();
        int v = p.second;
        if(dist[v] < p.first) continue;
 
        for(int i=0; i<g[v].size(); ++i) {
          Edge &e = g[v][i];
          if(e.cap > 0 && dist[e.to] > dist[v] + e.cost + h[v] - h[e.to]) {
            dist[e.to] = dist[v] + e.cost + h[v] - h[e.to];
            prv_v[e.to] = v; prv_e[e.to] = i;
            que.push(P(dist[e.to], e.to));
          }
        }
      }
      if(dist[t] == inf) {
        return -1;
      }
      for(int i=0; i<n; ++i) h[i] += dist[i];
 
      ll d = f;
      int v = t;
      while(v != s) {
        d = min(d, (ll) g[prv_v[v]][prv_e[v]].cap);
        v = prv_v[v];
      }
      f -= d;
      res += d * h[t];
      v = t;
      while(v != s) {
        Edge &e = g[prv_v[v]][prv_e[v]];
        e.cap -= d;
        g[v][e.rev].cap += d;
        v = prv_v[v];
      }
    }
    return res;
  }
};