const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((r) => r.split(" ").map(Number));
const [N, M] = input.shift();
const cards = input[0];
let visited = [...Array(N)].map(() => 0);
let ans = 0;

function dfs(depth, number) {
  if (depth === 3) {
    if (number > ans && number <= M) ans = number;
    return;
  }
  for (let i = 0; i < N; i++) {
    if (visited[i]) continue;
    visited[i] = 1;
    dfs(depth + 1, number + cards[i]);
    visited[i] = 0;
  }
  return ans;
}
console.log(dfs(0, 0));
