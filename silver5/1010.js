const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((t) => t.split(" ").map(Number));
input.shift();
for (let testCase of input) {
  solution([testCase[1], testCase[0], testCase[1] - testCase[0]]);
}

function solution([M, N, M_Minus_N]) {
  M = factorial(BigInt(M));
  N = factorial(BigInt(N));
  M_Minus_N = factorial(BigInt(M_Minus_N));
  console.log(Number(M / N / M_Minus_N));
}

function factorial(num) {
  let dp = [0n, 1n];

  for (let i = 2; i <= BigInt(num); i++) {
    dp[i] = dp[dp.length - 1] * BigInt(i);
  }
  return dp[dp.length - 1];
}
