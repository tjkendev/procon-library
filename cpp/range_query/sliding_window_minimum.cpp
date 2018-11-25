// DequeSlide
// 数列x_1, ..., x_nについてx_i, ..., x_{i+k}の最小値を求める
// DequeSlide(n: 配列数, l: kの値)
// push: 値(x_j)を追加
// get: x_i, ..., x_{i+k}の最小値を取得
// debug: デバッグ用
template<class T>
class DequeSlide {
  T *data;
  int *deq;
  int n, l, s, t;
  int cur;

public:
  DequeSlide(int n, int l) {
    data = new T[n];
    deq = new int[n];
    this->n = n;
    this->l = l;
    s = t = cur = 0;
  }

  void push(T x) {
    if(s<t && deq[s] == cur-l) s++;
    while(s<t && data[deq[t-1]] >= x) t--;
    deq[t++] = cur;
    data[cur++] = x;
  }

  T get() {
    return data[deq[s]];
  }

  void debug() {
    cout << s << " " << t << " [";
    repl(i, s, t-1) {
      cout << " " << data[deq[i]];
    }
    cout << " ]" << endl;
  }
};
