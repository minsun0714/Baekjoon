const inputFileName =
  process.platform === "linux" ? "/dev/stdin" : "example.txt";

const input = require("fs").readFileSync(inputFileName).toString().trim();
const N = Number(input);

let dp = [0, 1, 2];

for (let i = 3; i <= N; i++) {
  dp[i] = (dp[i - 1] + dp[i - 2]) % 15746;
}
console.log(dp[N] % 15746);
