const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
const freq = input.reduce((acc, cur) => {
  acc[cur] ? acc[cur]++ : (acc[cur] = 1);
  return acc;
}, {});
let ans = [];
for (let v in freq) freq[v] > 1 ? ans.push(v) : null;
ans.sort();
console.log(ans.length);
for (let v of ans) console.log(v);
