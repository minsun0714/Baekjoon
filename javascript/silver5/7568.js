const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((r) => r.split(" ").map(Number));

const N = input.shift()[0];
let ans = [];
for (let i = 0; i < N; i++) {
  let rank = 1;
  for (let j = 0; j < N; j++) {
    if (i === j) continue;
    [weightA, heightA] = input[i];
    [weightB, heightB] = input[j];

    if (weightA < weightB && heightA < heightB) rank++;
  }
  ans.push(rank);
}
console.log(ans.join(" "));
