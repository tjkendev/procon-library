import sys
readline = sys.stdin.readline
write = sys.stdout.write
flush = sys.stdout.flush

# クエリ: "? x1 x2" を出力
def query(x1, x2):
    write("? %d %d\n" % (x1, x2))
    flush()
    # ジャッジから返される値を取得
    return readline().strip()

# 回答: "! x" を出力
def answer(x):
    write("! %d\n" % x)
    flush()
    # 即時終了
    exit(0)