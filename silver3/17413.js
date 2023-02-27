const input = require("fs").readFileSync("example.txt").toString().trim();

let ans = "";
let temp = "";
let isOpen = false;

for (let i = 0; i < input.length; i++) {
  if (input[i] === "<") isOpen = true;
  if (isOpen || (!isOpen && input[i] === " ")) ans += input[i];

  if (!isOpen) {
    if (input[i] !== " ") temp = input[i] + temp;
    if (input[i + 1] === "<" || input[i + 1] === " " || !input[i + 1]) {
      ans += temp;
      temp = "";
    }
  }

  if (input[i] === ">") isOpen = false;
}
console.log(ans);
