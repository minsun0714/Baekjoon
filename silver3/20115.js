let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
input = input[0].split(" ").sort((a, b) => a - b);
input = input.reduce((acc, cur, i, a) => {
  acc += cur / 2;
  return acc;
}, input[input.length - 1] / 2);
console.log(input);
