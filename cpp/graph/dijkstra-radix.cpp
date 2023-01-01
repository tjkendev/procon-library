#include<vector>
using namespace std;

#define B 33

template<typename T>
class RadixHeap {
  struct Val {
    int x; T key;

    bool operator<(const Val &other) {
      return x < other.x;
    }
  };
  vector<Val> data[B];
  int last = 0, siz = 0;

  inline int bsr(int x) {
    if(x == 0) return -1;
    return 31-__builtin_clz(x);
  }

public:
  inline void push(T key, int x) {
    //assert(last <= x);
    ++siz;
    data[bsr(x^last)+1].emplace_back(Val{x, key});
  }

  inline Val pop() {
    //assert(siz > 0);
    if(!data[0].size()) {
      int i = 1;
      while(!data[i].size()) ++i;
      Val &em = *min_element(data[i].begin(), data[i].end());
      for(Val &e : data[i]) {
        if(e.key == em.key) {
          --siz;
          continue;
        }
        data[bsr(e.x^em.x)+1].emplace_back(e);
      }
      data[i].clear();
      return em;
    }
    --siz;
    Val &em = data[0].back();
    data[0].pop_back();
    return em;
  }

  inline bool empty() {
    return siz == 0;
  }

  inline int size() {
    return siz;
  }
};

struct Edge {
  int to; int cost;
};

const int inf = 1e9+1;

#define N 100004
int n;
vector<Edge> g[N];
int dist[N];

void dijkstra(int s) {
  RadixHeap<int> que;
  que.push(s, 0);
  for(int i=0; i<n; ++i) dist[i] = inf;
  dist[s] = 0;

  while(!que.empty()) {
    auto p = que.pop();
    int co = p.x; int v = p.key;
    if(dist[v] < co) continue;
    for(auto &e : g[v]) {
      if(co + e.cost < dist[e.to]) {
        dist[e.to] = co + e.cost;
        que.push(e.to, dist[e.to]);
      }
    }
  }
}
