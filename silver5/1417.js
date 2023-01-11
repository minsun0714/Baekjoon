const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
let dasom = Number(input[0]);

input.shift();
let candidates = input.map((v) => Number(v));

let count = 0;
while (dasom <= Math.max(...candidates)) {
  dasom += 1;
  candidates = candidates.map((v, i) =>
    i === candidates.indexOf(Math.max(...candidates)) ? (v -= 1) : v
  );
  count++;
}
console.log(count);
