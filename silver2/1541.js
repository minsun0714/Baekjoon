const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("-");
const arr = input.map((el) =>
  isNaN(+el) ? el.split("+").reduce((s, v) => s + +v, 0) : el
);
const res = arr.reduce((acc, cur) => acc - +cur);
console.log(res);
