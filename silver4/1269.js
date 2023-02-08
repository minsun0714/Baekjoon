let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
input = input.map((v) => v.split(" ")).flat();
input.sort((a, b) => a - b);
const dif = input.filter((v, i, a) => v !== a[i + 1] && v !== a[i - 1]);
console.log(dif.length);
