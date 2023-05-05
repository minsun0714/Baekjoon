let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map(Number));
input.shift();
while (input.length > 0) {
  const testCase = input.splice(0, 3);
  const size = testCase[0][0];
  const start = testCase[1];
  const end = testCase[2];
  console.log(solution(size, start, end));
}

function solution(size, start, end) {
  if (start[0] === end[0] && start[1] === end[1]) return 0;

  const dx = [-2, -2, 2, 2, -1, -1, 1, 1];
  const dy = [-1, 1, -1, 1, -2, 2, -2, 2];

  function bfs(x, y) {
    let queue = [];
    queue.push(start);

    let board = [...Array(size)].map((row) =>
      [...Array(size)].map((v) => (v = 0))
    );

    while (true) {
      if (board[end[0]][end[1]] > 0) return board[end[0]][end[1]];
      [x, y] = queue.shift();

      for (let i = 0; i < 8; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];

        if (nx < 0 || ny < 0 || nx >= size || ny >= size) continue;
        if (board[nx]?.[ny] > 0) continue;

        board[nx][ny] = board[x][y] + 1;

        queue.push([nx, ny]);
      }
    }
  }
  return bfs(start[0], start[1]);
}
