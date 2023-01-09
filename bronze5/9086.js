const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
for (let v of input) console.log(v[0] + v[v.length - 1]);
