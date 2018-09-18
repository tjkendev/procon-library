#define NN 30
 
struct TrieNode {
  TrieNode(int size) : sz(size), cnt(0) {
    for(int i = 0; i < NN; ++i) next[i] = nullptr;
    suffix = nullptr;
  }
  TrieNode *next[NN];
  TrieNode *suffix;
  int sz, cnt;
};
 
TrieNode *root = new TrieNode(0);
 
void add(string s) {
  TrieNode *node = root;
  for(int i = 0; i < s.length(); ++i) {
    int code = s[i] - 'a';
    if(!node->next[code]) {
      node = node->next[code] = new TrieNode(node->sz + 1);
    } else {
      node = node->next[code];
    }
  }
  node->cnt = 1;
}
 
void suffix() {
  queue<TrieNode*> que;
  que.push(root);
  while(!que.empty()) {
    TrieNode* v = que.front(); que.pop();
    for(int i = 0; i< NN; ++i) {
      if(v->next[i] && v->sz < v->next[i]->sz) {
        if(v->suffix) {
          v->next[i]->suffix = v->suffix->next[i];
        } else {
          v->next[i]->suffix = root;
        }
        que.push(v->next[i]);
      } else {
        if(v->suffix) {
          v->next[i] = v->suffix->next[i];
        } else {
          if(root->next[i]) {
            v->next[i] = root->next[i];
          } else {
            v->next[i] = root;
          }
        }
      }
    }
  }
  root->suffix = root;
}