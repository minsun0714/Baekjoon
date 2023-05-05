const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let isEnd = false;
let visited = [...Array(9)].map(() => 0);
let ans = [];

function dfs(depth, sum) {
  if (depth === 7 && sum === 100) {
    visited.forEach((n, i) => {
      if (n === 1) ans.push(input[i]);
    });

    ans.sort((a, b) => a - b);
    ans.forEach((v) => console.log(v));

    isEnd = true;
  }

  for (let i = 0; i < 9; i++) {
    if (isEnd || visited[i]) continue;

    visited[i] = 1;
    dfs(depth + 1, sum + input[i]);

    visited[i] = 0;
  }
}

dfs(0, 0);
