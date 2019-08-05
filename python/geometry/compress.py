# 入力: 座標の配列
# 出力 MP[e] = i: 座標eはi番目に該当
def compress(arr):
    *XS, = set(arr)
    XS.sort()
    return {e: i for i, e in enumerate(XS)}

# 1行バージョン
compress2 = lambda arr: {e: i for i, e in enumerate(sorted(set(arr)))}