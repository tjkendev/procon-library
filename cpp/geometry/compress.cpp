map<int, int> compress(const vector<int> &xs) {
  map<int, int> result;
  for(int i=0; i<xs.size(); ++i) {
    result[xs[i]] = 0;
  }
  int i = 0;
  for(auto it = result.begin(); it != result.end(); ++it, ++i) {
    result[(*it).first] = i;
  }
  return result;
}