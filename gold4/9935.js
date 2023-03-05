const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");

const [word, explodingWord] = [input[0], input[1]];
let stack = [];

word.split("").forEach((v) => {
  stack.push(v);
  if (stack.slice(-1 * explodingWord.length).join("") === explodingWord) {
    for (let i = 0; i < explodingWord.length; i++) {
      stack.pop();
    }
  }
});
console.log(stack.length ? stack.join("") : "FRULA");
