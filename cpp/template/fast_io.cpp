#include<cstdio>
using namespace std;

class FastIO {
  static const int rdata_sz = (1 << 25), wdata_sz = (1 << 25);
  char rdata[rdata_sz], wdata[wdata_sz], *rb, *wb;
  char tmp_s[20];

public:
  FastIO() {
    fread(rdata, 1, rdata_sz, stdin);
    rb = rdata; wb = wdata;
  }
  ~FastIO() {
    fwrite(wdata, 1, wb - wdata, stdout);
  }

  template<typename T>
  inline void read_i(T &x) {
    bool neg = false;
    x = 0;
    while((*rb < '0' || *rb > '9') && *rb != '-') ++rb;
    if(*rb == '-') {
      neg = true;
      ++rb;
    }
    while('0' <= *rb && *rb <= '9') {
      x = 10 * x + (*rb - '0');
      ++rb;
    }
    if(neg) x = -x;
  }

#define pc(x) *(wb++) = x
  template<typename T>
  inline void writeln_i(T x) {
    if (x == 0) { pc('0'); pc('\n'); return; }
    if(x < 0) { pc('-'); x = -x; }
    char *t = tmp_s;
    while(x) {
      T y = x / 10;
      *(t++) = (x - y*10) + '0';
      x = y;
    }
    while(t != tmp_s) pc(*(--t));
    pc('\n');
  }
#undef pc
};
FastIO io;
