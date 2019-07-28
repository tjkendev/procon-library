#include<vector>
using namespace std;
using ll = long long;


struct Pos {
  ll x, y;
 
  bool operator< (const Pos& other) const {
    return (x == other.x ? y < other.y : x < other.x);
  }
};
 
inline ll cross(Pos &a, Pos &b, Pos &c) {
  return (((b.x - a.x) * (c.y - a.y)) - ((b.y - a.y) * (c.x - a.x)));
}
 
void convex_hull(vector<Pos> &ps, vector<Pos> &qs) {
  // sort(ps.begin(), ps.end());
  qs.clear();
  qs.reserve(ps.size());
  int n = ps.size();
  for(auto p : ps) {
    // 外積判定の等号なし => 凸包の直線上にある点も含む
    while(qs.size() > 1 && cross(qs[qs.size()-2], qs[qs.size()-1], p) > 0) {
      qs.pop_back();
    }
    qs.push_back(p);
  }
  int t = qs.size();
 
  for(int i = n-2; i >= 0; --i) {
    Pos &p = ps[i];
    while(qs.size() > t && cross(qs[qs.size()-2], qs[qs.size()-1], p) > 0) {
      qs.pop_back();
    }
    qs.push_back(p);
  }
  qs.pop_back();
}