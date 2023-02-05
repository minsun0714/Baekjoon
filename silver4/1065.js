const n = require("fs").readFileSync("example.txt").toString().trim();
if (n < 100) {
  console.log(n);
  return;
}
function solution(n) {
  let count = 0;
  for (let i = 1; i <= n; i++) {
    new Set(isHan(i)).size < 2 ? count++ : count;
  }
  return count;
}

function isHan(n) {
  const arr = n.toString().split("");
  const ans = arr.map((v, i, a) => (i > 0 ? v - a[i - 1] : null));
  ans.shift();
  return ans;
}
console.log(solution(n));
