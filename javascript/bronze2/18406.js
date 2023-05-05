const input = require("fs").readFileSync("example.txt").toString().trim();
const ans = input
  .split("")
  .map(Number)
  .reduce(
    (acc, cur, index, arr) => {
      index < arr.length / 2 ? acc[0].push(cur) : acc[1].push(cur);
      return acc;
    },
    [[], []]
  );

function sum(arr) {
  return arr.reduce((s, v) => s + v);
}

console.log(sum(ans[0]) === sum(ans[1]) ? "LUCKY" : "READY");
