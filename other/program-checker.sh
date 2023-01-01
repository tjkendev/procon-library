# a program for generating testcase
gen="python3 gen.py"
# programs for check (execute these command with generated testcase)
prog1="python3 a.py"
prog2="./a.out"

while :; do
  $gen > input.txt
  out1=`$prog1 < input.txt`
  out2=`$prog2 < input.txt`

  if [ "\$out1" != "$out2" ]; then
    # failed
    echo "===== input ====="
    cat input.txt
    echo "===== output1 '$prog1' ====="
    echo $out1
    echo "===== output2 '$prog2' ====="
    echo $out2
    break
  fi
done
