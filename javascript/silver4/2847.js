const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((v) => +v);
input.shift();
const l = input.length;
let target = 0;
let ans = 0;
for (let i = 0; i < l; i++) {
  const last = input.pop();
  target = target || last;
  if (input[input.length - 1] >= target) {
    target -= 1;
    ans += input[input.length - 1] - target;
  } else {
    target = 0;
  }
}
console.log(ans);
