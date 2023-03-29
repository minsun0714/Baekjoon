const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((r) => r.split(" ").map(Number));
const [N, L] = input[0];
input.shift();
const arr = input[0];
arr.sort((a, b) => a - b);
let count = 0;
while (arr.length) {
  const tapeEnd = arr[arr.length - 1];
  const tapeStart = tapeEnd - (L - 1);
  while (arr[arr.length - 1] >= tapeStart) {
    arr.pop();
  }
  count++;
}
console.log(count);
