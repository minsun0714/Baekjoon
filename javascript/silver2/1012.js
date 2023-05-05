const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map(Number));
input.shift();

while (input.length) {
  const l = input[0][2];
  console.log(solution(input.splice(0, l + 1)));
}

function solution(arr) {
  const [M, N, K] = arr.shift();
  let marking = [...Array(M)].map((_) => [...Array(N)].map((r) => 0));
  arr.forEach(([i, j]) => (marking[i][j] = 1));

  function dfs(x, y) {
    if (x < 0 || y < 0 || x >= M || y >= N) return false;
    if (marking[x][y] === 0) return false;

    marking[x][y] = 0;

    dfs(x - 1, y);
    dfs(x + 1, y);
    dfs(x, y - 1);
    dfs(x, y + 1);

    return marking;
  }

  let ans = 0;
  for (let i = 0; i < M; i++) {
    for (let j = 0; j < N; j++) {
      if (dfs(i, j)) ans++;
    }
  }
  return ans;
}
