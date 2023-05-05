const input = Number(
  require("fs").readFileSync("example.txt").toString().trim()
);

let dp = [0, 1, 3];
for (let i = 3; i <= input; i++) {
  dp[i] = (2 * dp[i - 2] + dp[i - 1]) % 10007;
}
console.log(dp[input] % 10007);
