const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
for (let testCase of input) console.log(solution(Array.from(testCase)));

function solution(testCase) {
  let stack = [];

  while (testCase.length) {
    stack.push(testCase.shift());
    if (stack.slice(-2).join("") === "()") {
      stack.pop();
      stack.pop();
    }
  }
  return stack.length ? "NO" : "YES";
}
