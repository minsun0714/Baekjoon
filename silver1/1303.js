const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
const [N, M] = input[0].split(" ");
input.shift();
let board = input.slice().map((r) => r.split(""));

let [white, black] = [0, 0];

function dfs(x, y, team) {
  if (x < 0 || y < 0 || x >= N || y >= M) {
    return false;
  }
  if (board[x][y] === "X") return false;

  if (!team) {
    team = board[x][y] === "W" ? "myTeam" : "yourTeam";
  }

  if (
    (team === "myTeam" && board[x][y] === "B") ||
    (team === "yourTeam" && board[x][y] === "W")
  ) {
    return false;
  }

  board[x][y] = "X";
  team === "myTeam" ? white++ : black++;

  dfs(x - 1, y, team);
  dfs(x + 1, y, team);
  dfs(x, y - 1, team);
  dfs(x, y + 1, team);

  return team === "myTeam" ? ["W", white ** 2] : ["B", black ** 2];
}

let [totalW, totalB] = [0, 0];

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    const res = dfs(i, j);
    if (!res) continue;

    let [team, score] = res;
    if (team === "W") totalW += score;
    else totalB += score;
    white = 0;
    black = 0;
    team = "";
  }
}
console.log(totalW, totalB);
