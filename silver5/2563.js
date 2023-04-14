const inputFileName =
  process.platform === "linux" ? "/dev/stdin" : "example.txt";
const input = require("fs")
  .readFileSync(inputFileName)
  .toString()
  .trim()
  .split("\n")
  .map((r) => r.split(" ").map(Number));
const [N, ...areas] = input;
const totalArea = N * 100;
let overlappingArea = 0;
const obj = {};

for (const [x, y] of areas) {
  solution(x, y);
}

function solution(x, y) {
  for (let i = y; i < y + 10; i++) {
    if (!obj[i]) obj[i] = [];
    for (let j = x; j < x + 10; j++) {
      if (!obj[i].includes(j)) {
        obj[i].push(j);
      } else {
        overlappingArea++;
      }
    }
  }
}

console.log(totalArea - overlappingArea);
