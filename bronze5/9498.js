const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
const score = Number(input[0]);
console.log(score);
if (score >= 90) console.log("A");
else if ((score < 90) & (score >= 80)) console.log("B");
else if ((score < 80) & (score >= 70)) console.log("C");
else if ((score < 70) & (score >= 60)) console.log("D");
else console.log("F");
