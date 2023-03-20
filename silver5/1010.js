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

function solution([a, b, c]) {
  a = factorial(BigInt(a));
  b = factorial(BigInt(b));
  c = factorial(BigInt(c));
  console.log(Number(a / b / c));
}

function factorial(num) {
  let dp = [0n, 1n];

  for (let i = 2; i <= BigInt(num); i++) {
    dp[i] = dp[dp.length - 1] * BigInt(i);
  }
  return dp[dp.length - 1];
}
