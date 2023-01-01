
/* 全列挙
 * vector<T> (N) --> set<T> (2^N)
 */
template<typename T>
set<T> enum_make(vector<T>& vs) {
  set<T> s;
  s.insert(0);
  for(int i=0; i<vs.size(); ++i) {
    T &e = vs[i];
    set<T> s2;
    for(set<T>::iterator it=s.begin(); s!=s.end(); ++it) {
      s2.insert(*it);
      s2.insert((*it) + e);
    }
    s = s2;
  }
  return s;
}

/* 全列挙C++11 */
template<typename T>
set<T> enum_make(vector<T> &vs) {
  set<T> s {0};
  for(T e : vs) {
    set<T> s2;
    for(T v : s) {
      s2.insert(v);
      s2.insert(v + e);
    }
    s = s2;
  }
  return s;
}
