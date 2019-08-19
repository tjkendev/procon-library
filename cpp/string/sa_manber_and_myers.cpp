#include<string>
#include<algorithm>
using namespace std;

#define L (1 << 17)

struct SuffixArray {
  int tmp[L];
  int rank[L], sa[L], lcp[L], n;
  string s;

  SuffixArray(string s) : s(s) {}

  void construct_suffix() {
    n = s.length();
    for(int i=0; i<=n; ++i) {
      sa[i] = i;
      rank[i] = (i < n ? s[i] : -1);
    }

    int k = 1;
    auto sa_cmp = [=](int i, int j) -> bool {
      if(rank[i] != rank[j]) {
        return rank[i] < rank[j];
      }
      int ri = (i+k <= n ? rank[i+k] : -1);
      int rj = (j+k <= n ? rank[j+k] : -1);
      return ri < rj;
    };
    while(k <= n) {
      sort(sa, sa + n+1, sa_cmp);
      tmp[sa[0]] = 0;
      for(int i=1; i<=n; ++i) {
        tmp[sa[i]] = tmp[sa[i-1]] + sa_cmp(sa[i-1], sa[i]);
      }
      for(int i=0; i<=n; ++i) rank[i] = tmp[i];
      k <<= 1;
    }
  }

  void construct_lcp() {
    for(int i=0; i<=n; ++i) lcp[i] = -1, rank[sa[i]] = i;

    int h = 0;
    lcp[0] = 0;
    for(int i=0; i<n; ++i) {
      int j = sa[rank[i] - 1];

      if(h > 0) --h;
      while(j + h < n && i + h < n && s[j+h] == s[i+h]) ++h;
      lcp[rank[i] - 1] = h;
    }
  }
};
