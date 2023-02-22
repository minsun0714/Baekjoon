let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
input.sort((a, b) => b - a);
input = input.map((v, i) => Math.max(0, v - i));
console.log(input.reduce((s, v) => s + v, 0));
