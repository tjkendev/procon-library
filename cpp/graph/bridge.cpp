#include<vector>
#include<map>
using namespace std;
using P = pair<int, int>;


#define N 100006
 
int n, m;
vector<int> g[N];
 
vector<P> bs;
int used[N], val[N];
int dfs(int v, int p) {
  int res = 0, cnt = 0;
  used[v] = 1; // searching
  for(int w : g[v]) {
    if(w == v) {
      // self-loop edge
      continue;
    }
    if(w == p) {
      if(cnt > 0) {
        // (p, v): multiple edges
        res += 1;
        val[w] += 1;
      }
      ++cnt;
      continue;
    }
    if(!used[w]) {
      res += dfs(w, v);
    } else if(used[w] == 1) {
      res += 1;
      val[w] += 1;
    }
  }
  used[v] = 2; // searched
  res -= val[v];
 
  if(p != -1 && res == 0) {
    bs.push_back(p < v ? P(p, v) : P(v, p));
  }
  return res;
}
 
void bridge() {
  bs.clear();
  for(int i=0; i<n; ++i) used[i] = used[i] = 0;
  dfs(0, -1);
}