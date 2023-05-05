const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);
input.shift();
input.forEach((n) => console.log(solution(n)));

function solution(n) {
  let dp = [0, 1, 2, 4];

  for (let i = 4; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
  }
  return dp[n];
}
