let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map(Number));

const [H, W] = input.shift();
const empty = input[0].map((v) => H - v);

let blocks = [...new Array(H)].map((_) => [...new Array(W)]);
blocks = blocks.map((row, i) =>
  row.map((_, j) => {
    if (i < [empty[j]]) return 0;
    else return 1;
  })
);

let count = 0;
for (let i = 0; i < H; i++) {
  blocks = blocks.map((row) => {
    return row.map((v, j) => {
      if (
        v === 0 &&
        row.filter((_, index) => index < j).some((el) => el === 1) &&
        row.filter((_, index) => index > j).some((el) => el === 1)
      )
        count++;
    });
  });
}
console.log(count);
