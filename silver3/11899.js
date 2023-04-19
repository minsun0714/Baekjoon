const inputFileName =
  process.platform === "linux" ? "/dev/stdin" : "example.txt";

const input = require("fs")
  .readFileSync(inputFileName)
  .toString()
  .trim()
  .split("");
let stack = [];
input.forEach((p) => {
  stack.push(p);
  if (stack.slice(-2).join("") === "()") {
    stack.pop();
    stack.pop();
  }
});
console.log(stack.length);
