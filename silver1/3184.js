const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
const [R, C] = input[0].split(" ").map(Number);
input.shift();
const field = input.map((r) => r.split(""));

let sheep = 0;
let wolf = 0;
function dfs(x, y) {
  if (x < 0 || y < 0 || x >= R || y >= C) return false;
  if (field[x][y] === "#") return false;

  if (field[x][y] === "o") sheep++;
  if (field[x][y] === "v") wolf++;

  field[x][y] = "#";

  dfs(x - 1, y);
  dfs(x + 1, y);
  dfs(x, y - 1);
  dfs(x, y + 1);

  return [sheep, wolf];
}

let [totalSheep, totalWolf] = [0, 0];
for (let i = 0; i < R; i++) {
  for (let j = 0; j < C; j++) {
    const area = dfs(i, j);
    if (!area || (!sheep && !wolf)) continue;

    if (sheep > wolf) wolf = 0;
    if (sheep <= wolf) sheep = 0;

    totalSheep += sheep;
    totalWolf += wolf;

    sheep = 0;
    wolf = 0;
  }
}
console.log(totalSheep, totalWolf);
