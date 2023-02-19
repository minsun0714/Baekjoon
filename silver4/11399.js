let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
input = input[0]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);
let arr = [];
input = input.reduce((acc, cur) => {
  acc += cur;
  arr.push(acc);
  return acc;
}, 0);
console.log(arr.reduce((s, v) => s + v, 0));
