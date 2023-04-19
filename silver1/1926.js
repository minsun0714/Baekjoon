const inputFileName =
  process.platform === "linux" ? "/dev/stdin" : "example.txt";

const input = require("fs")
  .readFileSync(inputFileName)
  .toString()
  .trim()
  .split("\n")
  .map((r) => r.split(" ").map(Number));
const [[n, m], ...board] = input;

let area = 0;
function dfs(x, y) {
  if (x < 0 || y < 0 || x >= n || y >= m) return false;
  if (board[x][y] === 0) return false;

  board[x][y] = 0;
  area++;

  dfs(x - 1, y);
  dfs(x + 1, y);
  dfs(x, y - 1);
  dfs(x, y + 1);

  return area;
}

let count = 0;
let ansArea = 0;

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    const res = dfs(i, j);
    if (res) {
      count++;
      if (res > ansArea) {
        ansArea = res;
      }
      area = 0;
    }
  }
}
console.log(count);
console.log(ansArea);
