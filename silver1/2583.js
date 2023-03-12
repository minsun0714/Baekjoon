let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map(Number));
const [M, N, K] = input[0];
input.shift();

let paper = [...Array(M)].map((row) => [...Array(N)].map((v) => 0));
paper.forEach((row, i) =>
  row.forEach((_, j) => {
    for (let sqr of input) {
      if (i >= sqr[1] && i < sqr[3] && j >= sqr[0] && j < sqr[2]) {
        paper[i][j] = 1;
      }
    }
  })
);
let countBlank = 0;
function dfs(x, y) {
  if (paper[x]?.[y] === 1) return false;
  if (x < 0 || y < 0 || x >= M || y >= N) return false;
  countBlank++;
  paper[x][y] = 1;
  dfs(x - 1, y);
  dfs(x, y - 1);
  dfs(x + 1, y);
  dfs(x, y + 1);

  return paper;
}

let answer = 0;
let result = [];
for (let i = 0; i < M; i++) {
  for (let j = 0; j < N; j++) {
    if (dfs(i, j)) {
      answer++;
      result.push(countBlank);
      countBlank = 0;
    }
  }
}
console.log(answer);
result.sort((a, b) => a - b);
console.log(result.join(" "));
