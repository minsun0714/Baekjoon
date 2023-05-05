let input = Number(require("fs").readFileSync("example.txt").toString().trim());
const INF = Number.POSITIVE_INFINITY;
input = 5;
let dp = [0, INF];
for (let i = 2; i <= input; i++) {
  if (i === 2 || i === 5) {
    dp[i] = 1;
    continue;
  }
  const fiveBefore = dp[i - 5] || INF;
  const twoBefore = dp[i - 2] || INF;
  dp[i] = Math.min(fiveBefore, twoBefore) + 1;
}
const ans = dp[input];
console.log(ans === INF ? -1 : ans);
