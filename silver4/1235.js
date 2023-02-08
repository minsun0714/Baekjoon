const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(""));
input.shift();
let count = 0;
for (let i = 1; i <= input[0].length; i++) {
  count++;
  let arr = [];
  for (let v of input) {
    arr.push(v.slice(-1 * i).join(""));
  }
  console.log(arr);
  if (arr.length === [...new Set(arr)].length) {
    console.log(count);
    break;
  }
}
