const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("");
console.log(solution(input));

function solution(input) {
  let stack = [];
  let stick = 0;
  let ans = 0;

  input.forEach((p, i, a) => {
    stack.push(p);
    if (p === "(") {
      if (a[i + 1] === "(") {
        stick++;
      }
    } else {
      stack.pop();
      stack.pop();
      if (a[i - 1] === "(") {
        ans += stick;
      } else {
        ans++;
        stick--;
      }
    }
  });
  return ans;
}
