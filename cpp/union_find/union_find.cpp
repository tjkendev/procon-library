#define N 100008

int parent[N];
int root(int x) {
  if(x == parent[x]) {
    return x;
  }
  return parent[x] = root(parent[x]);
}

bool unite(int x, int y) {
  int px = root(x), py = root(y);
  if(px == py) return false;

  if(px < py) {
    parent[py] = px;
  } else {
    parent[px] = py;
  }
  return true;
}

// 以下で初期化
//
// rep(i, n) parent[i] = i;
//