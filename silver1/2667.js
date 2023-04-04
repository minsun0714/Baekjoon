const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
const N = input.shift();
let board = input.map((r) => r.split("").map(Number));

let count = 0;
function dfs(x, y) {
  if (x < 0 || y < 0 || x >= N || y >= N) {
    return false;
  }
  if (board[x][y] === 0) return false;

  count++;
  board[x][y] = 0;

  dfs(x - 1, y);
  dfs(x + 1, y);
  dfs(x, y - 1);
  dfs(x, y + 1);

  return count;
}
let ans = 0;
let arr = [];
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    const res = dfs(i, j);
    if (res) {
      arr.push(res);
      count = 0;
      ans++;
    }
  }
}
arr.sort((a, b) => a - b);
console.log(ans);
arr.forEach((v) => console.log(v));
