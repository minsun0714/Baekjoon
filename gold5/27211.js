const inputFileName =
  process.platform === "linux" ? "/dev/stdin" : "example.txt";

const input = require("fs")
  .readFileSync(inputFileName)
  .toString()
  .trim()
  .split("\n")
  .map((r) => r.split(" ").map(Number));

const [[N, M], ...planet] = input;

function dfs(x, y) {
  const stack = [[x, y]];
  planet[x][y] = 1;

  while (stack.length) {
    const [x, y] = stack.pop();
    console.log(x, y);

    function push(nx, ny) {
      if (planet[nx][ny] === 0) {
        stack.push([nx, ny]);
        planet[nx][ny] = 1;
      }
    }

    if (x > 0) push(x - 1, y);
    if (x < N - 1) push(x + 1, y);
    if (y > 0) push(x, y - 1);
    if (y < M - 1) push(x, y + 1);
    if (x === 0) push(N - 1, y);
    if (x === N - 1) push(0, y);
    if (y === 0) push(x, M - 1);
    if (y === M - 1) push(x, 0);
  }
}

let count = 0;
for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (planet[i][j] === 0) {
      dfs(i, j);
      count++;
    }
  }
}
console.log(count);
