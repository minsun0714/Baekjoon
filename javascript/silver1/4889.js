let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
input.pop();
let testNum = 0;
for (let v of input) {
  testNum++;
  console.log(solution(testNum, v));
}

function solution(testNum, v) {
  let stack = [];
  v.split("").forEach((paren) => {
    stack.push(paren);
    if (stack.slice(-2).join("") === "{}") {
      stack.pop();
      stack.pop();
    }
  });

  let count = 0;
  let stackAns = [];
  stack.forEach((paren) => {
    stackAns.push(paren);
    if (stackAns.slice(-2).join("") === "}{") {
      stackAns.pop();
      stackAns.pop();
      count += 2;
    } else if (stackAns.slice(-2).join("") === "}}") {
      stackAns.pop();
      stackAns.pop();
      count++;
    } else if (stackAns.slice(-2).join("") === "{{") {
      stackAns.pop();
      stackAns.pop();
      count++;
    }
  });
  return testNum + ". " + count;
}
