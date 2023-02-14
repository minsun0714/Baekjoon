let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(" ");
let stack = [];
for (let i = 2; i <= Number(input[0]); i++) {
  for (let j = 2; j <= Number(input[0]); j++)
    if (j % i === 0 && !stack.includes(j)) stack.push(j);
}
console.log(stack[Number(input[1]) - 1]);
