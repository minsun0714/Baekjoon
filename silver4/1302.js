let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
const freq = Object.entries(
  input.reduce((acc, cur) => {
    acc[cur] ? acc[cur]++ : (acc[cur] = 1);
    return acc;
  }, [])
);
const max = Math.max(...freq.map((v) => v[1]));
const ans = freq.filter((v) => v[1] === max);
console.log(ans.map((v) => v[0]).sort()[0]);
