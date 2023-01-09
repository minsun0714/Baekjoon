const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(" ");
const A = Number(input[0]);
const B = Number(input[1]);
console.log(A + B);
console.log(A - B);
console.log(A * B);
console.log(parseInt(A / B));
console.log(A % B);
