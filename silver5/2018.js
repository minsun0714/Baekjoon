const input = require("fs").readFileSync("example.txt").toString().trim();
function sol(n) {
  let count = 0;
  for (let i = 1; i <= n; i++) {
    let num = i;
    let stack = 0;
    while (stack < n) {
      stack += num;
      num++;
    }
    stack === n ? count++ : count;
  }
  return count;
}
console.log(sol(Number(input)));
