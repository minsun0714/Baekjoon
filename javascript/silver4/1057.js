let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(" ");

let [kim, lim] = [Number(input[1]), Number(input[2])];
let count = 0;
while (kim !== lim) {
  kim = Math.ceil(kim / 2);
  lim = Math.ceil(lim / 2);
  count++;
}
console.log(count);
