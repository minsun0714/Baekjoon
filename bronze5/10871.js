const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
const X = Number(input[0].split(" ")[1]);
const arr = input[1].split(" ");
for (let v of arr) v < X ? console.log(v) : null;
