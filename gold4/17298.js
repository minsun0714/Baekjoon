const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n")
  .map((r) => r.split(" ").map(Number));
const [[N], nums] = input;

const stackIndex = [];
const result = new Array(N).fill(-1);

for (let i = 0; i < N; i++) {
  while (
    stackIndex.length > 0 &&
    nums[i] > nums[stackIndex[stackIndex.length - 1]]
  ) {
    let top = stackIndex.pop();
    result[top] = nums[i];
  }
  stackIndex.push(i);
}

let answer = "";
for (let i = 0; i < N; i++) {
  answer += result[i] + " ";
}

process.stdout.write(answer.trim());
