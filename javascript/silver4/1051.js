const n = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
let max_size = n[0].split(" ")[0] - 1;
n.shift();

function isMax(n, max_size) {
  let arr = [];
  n.forEach((row, i, a) =>
    row.split("").map((v, j, row) => {
      v === row[j + max_size] &&
      v === a[i + max_size]?.[j] &&
      v === a[i + max_size]?.[j + max_size]
        ? arr.push([i, j])
        : null;
    })
  );
  return arr.length > 0 ? (max_size + 1) ** 2 : isMax(n, max_size - 1);
}

console.log(isMax(n, max_size));
