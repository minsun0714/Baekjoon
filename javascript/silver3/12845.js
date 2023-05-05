let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
input = input[0].split(" ").map(Number);
input.sort((a, b) => b - a);
let gold = 0;
for (let i = 1; i < input.length; i++) {
  gold += input[i] + input[0];
}
console.log(gold);
