declare function require(x: string): any;

class Scanner {
  private inputs: string[];
  private index: number;

  constructor(input : string) {
    this.inputs = input.toString().trim().split(/[ \n]/);
    this.index = 0;
  }

  next(): string {
    return this.inputs[this.index++];
  }

  nextInt(): number {
    return Number(this.next());
  }
}
let cin:Scanner = new Scanner(require('fs').readFileSync('/dev/stdin', 'utf8'));

class Main {
  public static main(): void {
    // do something
  }
}

Main.main();
