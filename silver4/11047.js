let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
let target = Number(input[0].split(" ")[1]);
input.shift();
input = input
  .filter((v) => v <= target)
  .reverse()
  .map(Number);

let count = 0;
while (target > 0) {
  count += parseInt(target / input[0]);
  target %= input[0];
  input.shift();
}
console.log(count);
