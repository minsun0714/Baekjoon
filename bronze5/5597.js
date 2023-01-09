const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
const allStudents = [...Array(30)].map((_, i) => i + 1);
let ans = [];
for (let v of allStudents) !input.includes(String(v)) ? ans.push(v) : null;
ans.sort((a, b) => a - b);
for (let v of ans) console.log(Number(v));
