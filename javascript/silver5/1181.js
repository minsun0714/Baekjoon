const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
const words = [...new Set(input)];

const length = words.sort().sort((a, b) => a.length - b.length);
for (let v of length) console.log(v);
