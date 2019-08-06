#include<vector>
#include<queue>
using namespace std;
using ll = long long;


#define N 100003
const ll inf = 1e10;

struct Node {
  ll cost; int v;

  bool operator>(const Node &other) const { return cost > other.cost; }
};
using p_queue = priority_queue<Node, vector<Node>, greater<Node> >;

struct Edge {
  int to; ll cost;
};
vector<Edge> g[N]; // 入力: グラフG

int n;
ll dist[N]; // 出力: 各頂点vの距離dist[v]

// 始点sから各頂点までの距離を計算
void dijkstra(int s) {
  p_queue que;
  que.emplace(Node{0, s});
  for(int i=0; i<n; ++i) dist[i] = inf;
  dist[s] = 0;

  while(!que.empty()) {
    Node nd = que.top();
    ll co = nd.cost; int v = nd.v;
    que.pop();
    if(dist[v] < co) continue;
    for(auto &e : g[v]) {
      if(co + e.cost < dist[e.to]) {
        dist[e.to] = co + e.cost;
        que.emplace(Node{dist[e.to], e.to});
      }
    }
  }
}