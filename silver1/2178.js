const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((row) => row.split(""));
const [N, M] = [
  Number(input[0].join("").split(" ")[0]),
  Number(input[0].join("").split(" ")[1]),
];
input.shift();
console.log(solution(0, 0));

function solution(x, y) {
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];
  let marking = [...Array(N)].map((_) => [...Array(M)].map((v) => (v = 1)));
  let queue = [];
  queue.push([x, y]);

  function bfs(x, y) {
    while (true) {
      [x, y] = queue.shift();

      if (marking[N - 1][M - 1] > 1) return marking[N - 1][M - 1];
      for (let i = 0; i < 4; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];

        if (input[nx]?.[ny] === "0") continue;
        if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
        if (marking[nx][ny] > 1) continue;
        marking[nx][ny] = marking[x][y] + 1;
        queue.push([nx, ny]);
      }
    }
  }
  return bfs(0, 0);
}
