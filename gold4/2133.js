const inputFileName =
  process.platform === "linux" ? "/dev/stdin" : "example.txt";

let N = Number(require("fs").readFileSync(inputFileName).toString().trim());
let dp = [1, 0, 3];

for (let i = 3; i <= N; i++) {
  if (i % 2 === 1) {
    dp[i] = 0;
    continue;
  }

  const base = [...Array(i / 2 + 1)].map((_, j) => 2 * j);
  dp[i] =
    dp[i - 2] * 3 +
    base.reduce((s, v, k) => (k > 1 ? s + dp[i - v] : null)) * 2;
}
console.log(dp[N]);
