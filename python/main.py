# Windows IDLE用 テストケースをコピペで処理できるように
# (C-dで入力終了)
# submit時には削除する
import sys
def raw_input_generator():
    for s in sys.stdin.readlines():
        for ss in s.strip().split('\n'):
            yield ss.strip()
raw_gen = raw_input_generator()
raw_input = lambda: raw_gen.next()
input = lambda: eval(raw_gen.next())

# 基本テンプレ
input = lambda x="": int(raw_input(x))
inputs = map(int, raw_input().split())
