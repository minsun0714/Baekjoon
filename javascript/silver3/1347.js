const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
let dx = [0];
let dy = [0];
let [x, y] = [0, 0];
input.shift();
const moves = input[0].split("");
let currentDir = 0;
moves.forEach((move) => {
  if (move === "R") {
    currentDir === 3 ? (currentDir = 0) : currentDir++;
  } else if (move === "L") {
    currentDir === 0 ? (currentDir = 3) : currentDir--;
  } else {
    switch (currentDir) {
      case 0:
        x += 1;
        break;
      case 1:
        y -= 1;
        break;
      case 2:
        x -= 1;
        break;
      case 3:
        y += 1;
        break;
    }
    dx.push(x);
    dy.push(y);
  }
});
while (dx.some((v) => v < 0)) {
  dx = dx.map((v) => (v += 1));
}
while (dy.some((v) => v < 0)) {
  dy = dy.map((v) => (v += 1));
}

const rowSize = Math.max(...dx) - Math.min(...dx) + 1;
const colSize = Math.max(...dy) - Math.min(...dy) + 1;
let ans = [...Array(rowSize)].map((_) => [...Array(colSize)]);

dx.forEach((rowNumber, i) => (ans[rowNumber][dy[i]] = "."));
ans = ans.map((row) => row.map((v) => (v ? v : "#")).join(""));
for (let row of ans) console.log(row);
