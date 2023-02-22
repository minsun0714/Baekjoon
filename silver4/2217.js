let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);
input.shift();
input.sort((a, b) => b - a);

const arr = input.map((v, i) => v * (i + 1));
console.log(Math.max(...arr));
