const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();

let count = 0;
input.forEach((row, i, a) => {
  row.split("").forEach((el, j, row) => {
    if (el === "-" && row[j - 1] !== "-") {
      count++;
    } else if (el === "|" && a[i - 1]?.[j] !== "|") {
      count++;
    }
  });
});
console.log(count);
