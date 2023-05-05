const inputFileName =
  process.platform === "linux" ? "/dev/stdin" : "example.txt";

const input = require("fs")
  .readFileSync(inputFileName)
  .toString()
  .trim()
  .split("\n");
const [R, C] = input.shift().split(" ");
const board = input.map((r) => r.split(""));

let [sheep, wolf] = [0, 0];
function bfs(x, y) {
  if (x < 0 || y < 0 || x >= R || y >= C) return false;
  if (board[x][y] === "#") return false;

  if (board[x][y] === "k") sheep++;
  if (board[x][y] === "v") wolf++;
  board[x][y] = "#";

  bfs(x - 1, y);
  bfs(x + 1, y);
  bfs(x, y - 1);
  bfs(x, y + 1);

  return [sheep, wolf];
}

let [totalSheep, totalWolf] = [0, 0];
for (let i = 0; i < R; i++) {
  for (let j = 0; j < C; j++) {
    const res = bfs(i, j);
    if (!res) continue;
    let [s, w] = res;
    if (s > w) w = 0;
    else s = 0;
    totalSheep += s;
    totalWolf += w;
    [sheep, wolf] = [0, 0];
  }
}
console.log(totalSheep, totalWolf);
